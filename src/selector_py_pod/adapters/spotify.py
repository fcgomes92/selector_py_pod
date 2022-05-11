from selector_py_pod.models.episode import Episode
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


def map_episodes(episode) -> Episode:
    return Episode(episode.get('id'), episode.get('name'), episode.get('external_urls').get('spotify'), episode.get('images')[0])


class SpotifyAdapter:
    def __init__(self, config) -> None:
        self.market = config.get("SPOTIFY_MARKET")
        self.client = Spotify(auth_manager=SpotifyClientCredentials(client_id=config.get("SPOTIFY_CLIENT_ID"),
                                                                    client_secret=config.get("SPOTIFY_CLIENT_SECRET")))

    def get_episodes(self, show_id) -> list[Episode]:
        stp = 50
        get_eps = self.client.show_episodes

        r = get_eps(show_id, market=self.market, limit=stp)
        items = r.get('items', [])
        episodes = list(map(map_episodes, items))

        total = r.get('total')
        offsets = total // stp

        for idx in range(1, offsets + 1):
            offset = idx * stp
            rx = get_eps(show_id, market=self.market, limit=stp, offset=offset)
            extra_episodes = list(map(map_episodes, rx.get('items', [])))
            episodes.extend(extra_episodes)

        return episodes
