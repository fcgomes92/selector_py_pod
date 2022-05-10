from selector_py_pod.adapters.serial import SerialAdapter
from selector_py_pod.adapters.spotify import SpotifyAdapter
from selector_py_pod.adapters.twitter import TwitterAdapter
from selector_py_pod.adapters.youtube import YouTubeAdapter
from selector_py_pod.adapters.cli_arguments import args
from selector_py_pod.config import build_config

config = build_config(args.env)
adapters = {
    'spt': SpotifyAdapter(config),
    'ytb': YouTubeAdapter(config)
}
outputs = {
    'serial': SerialAdapter(config),
    'twitter': TwitterAdapter(config)
}
