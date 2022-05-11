import pytest
from selector_py_pod.domain.utils import parse_show_id


class TestParseShowId:
    def test_spotify_string(self):
        expected = ('spt', 'spotify:show:ABC123')
        assert parse_show_id('spt:spotify:show:ABC123') == expected

    def test_youtube_string(self):
        expected = ('ytb', 'ABC123')
        assert parse_show_id('ytb:ABC123') == expected
