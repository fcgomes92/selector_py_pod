from unittest.mock import patch

import pytest
from selector_py_pod.adapters.serial import SerialAdapter
from selector_py_pod.adapters.twitter import TwitterAdapter
from selector_py_pod.domain.config import build_adapters, build_outputs
from spotipy import oauth2


@pytest.fixture
def config():
    return {
        'SPOTIFY_MARKET': 'BR',
        'SPOTIFY_CLIENT_ID': 'AAA',
        'SPOTIFY_CLIENT_SECRET': 'AAA',
        'YOUTUBE_TOKEN': '',
        'OUTPUT_JSON': '',
        'TWITTER_CONSUMER_KEY': '',
        'TWITTER_CONSUMER_SECRET': '',
        'TWITTER_ACCESS_KEY': '',
        'TWITTER_ACCESS_SECRET': ''
    }


class TestBuildConfig:

    def test_build_adapter(self, config):
        adapters = build_adapters(config)
        assert 'spt' in adapters
        assert 'ytb' in adapters

    def test_build_outputs(self, config):
        outputs = build_outputs(config)
        assert 'serial' in outputs
        assert 'twitter' in outputs
