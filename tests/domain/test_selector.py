from unittest.mock import Mock

import pytest
from selector_py_pod.domain.selector import build_selection
from selector_py_pod.models.episode import Episode
from selector_py_pod.models.selection import Selection


@pytest.fixture
def adapter() -> Mock:
    return Mock()


class TestBuildSelection:
    def test_select_5_from_adapter(self, adapter: Mock):
        episode = Episode('1', '1', 'https://foo.bar', 'https://foo.bar')
        adapter.get_episodes.return_value = [episode]
        selection = build_selection('test', 'test', 'test_id', adapter)
        assert selection.name == 'test'
        assert selection.description == 'test'
        assert len(selection.episodes) == 5
        for e in selection.episodes:
            assert e.serialize() == episode.serialize()

    def test_select_1_from_adapter(self, adapter: Mock):
        episode = Episode('1', '1', 'https://foo.bar', 'https://foo.bar')
        adapter.get_episodes.return_value = [episode]
        selection = build_selection('test', 'test', 'test_id', adapter, k=1)
        assert selection.name == 'test'
        assert selection.description == 'test'
        assert len(selection.episodes) == 1
        for e in selection.episodes:
            assert e.serialize() == episode.serialize()
