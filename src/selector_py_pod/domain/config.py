from selector_py_pod.adapters.serial import SerialAdapter
from selector_py_pod.adapters.spotify import SpotifyAdapter
from selector_py_pod.adapters.twitter import TwitterAdapter
from selector_py_pod.adapters.youtube import YouTubeAdapter


def build_adapters(config):
    return {
        'spt': SpotifyAdapter(config),
        'ytb': YouTubeAdapter(config)
    }


def build_outputs(config):
    return {
        'serial': SerialAdapter(config),
        'twitter': TwitterAdapter(config)
    }
