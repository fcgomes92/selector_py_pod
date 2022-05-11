from random import choices

from selector_py_pod.models.selection import Selection


def build_selection(name: str, description: str, channel_id: str, adapter, k: int = 5) -> Selection:
    episodes = adapter.get_episodes(channel_id)
    return Selection(name, description, choices(episodes, k=k))
