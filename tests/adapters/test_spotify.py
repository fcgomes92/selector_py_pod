from unittest.mock import patch

import pytest
from selector_py_pod.adapters.spotify import SpotifyAdapter
from selector_py_pod.models.episode import Episode


@pytest.fixture
def config() -> dict:
    return {
        'SPOTIFY_MARKET': 'BR',
        'SPOTIFY_CLIENT_ID': 'AAA',
        'SPOTIFY_CLIENT_SECRET': 'AAA',
    }


@pytest.fixture
def raw_episode() -> dict:
    return {
        'id': 'foo',
        'name': 'foo',
        'external_urls': {
            'spotify': 'foo',
        },
        'images': [
            'foo'
        ]
    }


@pytest.fixture
def obj_episode() -> Episode:
    return Episode('foo', 'foo', 'foo', 'foo')


class TestSpotifyAdapter:
    def test_get_episodes(self, config, raw_episode, obj_episode):
        show_id = 'AAA'
        adapter = SpotifyAdapter(config)
        return_value = {'total': 1, 'items': [raw_episode]}
        with patch.object(adapter.client, 'show_episodes', return_value=return_value) as client:
            episodes = adapter.get_episodes(show_id)
            assert len(episodes) == 1
            assert episodes[0].serialize() == obj_episode.serialize()
            client.assert_called_once_with(show_id, market='BR', limit=50)

    def test_get_episodes_all_pages(self, config, raw_episode, obj_episode):
        show_id = 'AAA'
        adapter = SpotifyAdapter(config)
        return_value = {'total': 110, 'items': [
            {**raw_episode, id: idx} for idx in range(25)]}
        with patch.object(adapter.client, 'show_episodes', return_value=return_value) as client:
            episodes = adapter.get_episodes(show_id)
            assert len(episodes) == 75
            client.assert_called_with(
                show_id, market='BR', limit=50, offset=100)
            for e in episodes:
                assert e.serialize() == obj_episode.serialize()
