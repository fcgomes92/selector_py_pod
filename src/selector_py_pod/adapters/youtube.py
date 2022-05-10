from googleapiclient.discovery import build
from selector_py_pod.models.episode import Episode


def build_url(id):
    return f'https://youtu.be/{id}'


def map_video_ids_from_playlist(item):
    return item.get('contentDetails').get('videoId')


def map_videos(video_item) -> Episode:
    snippet = video_item.get('snippet')
    id = video_item.get('id')
    return Episode(id, snippet.get('title'), build_url(id), snippet.get('thumbnails').get('high'))


class YouTubeAdapter:
    def __init__(self, config: dict) -> None:
        self.key = config.get('YOUTUBE_TOKEN')
        self.service_name = 'youtube'
        self.api_version = 'v3'

    def _get_videos(self, service, upload_playlist_id, next_page_token=None):
        playlist_response = service.playlistItems().list(
            part='contentDetails',
            maxResults=500,
            playlistId=upload_playlist_id,
            pageToken=next_page_token
        ).execute()
        page_token = playlist_response.get('nextPageToken')
        video_ids = map(map_video_ids_from_playlist,
                        playlist_response.get('items', []))
        videos_response = service.videos().list(
            part='snippet', id=','.join(video_ids)).execute()
        episodes = list(map(map_videos, videos_response.get('items', [])))
        if (page_token):
            episodes.extend(self._get_videos(
                service, upload_playlist_id, page_token))
        return episodes

    def get_episodes(self, channel_id: str) -> list[Episode]:
        with build(self.service_name, self.api_version, developerKey=self.key) as service:
            search_response = service.channels().list(
                part='contentDetails',
                id=channel_id,
            ).execute()
            c = search_response.get('items')[0]
            playlists = c.get('contentDetails', {}).get('relatedPlaylists', {})
            upload_playlist_id = playlists.get('uploads')
            if upload_playlist_id:
                return self._get_videos(service, upload_playlist_id)
            else:
                return []
