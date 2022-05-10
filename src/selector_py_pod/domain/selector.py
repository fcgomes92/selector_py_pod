from random import choices

from selector_py_pod.domain.config import adapters, config, outputs
from selector_py_pod.domain.utils import parse_show_id
from selector_py_pod.models.selection import Selection


def build_selection(name: str, description: str, show_id: str, k: int = 5) -> Selection:
    adapter_name, channel_id = parse_show_id(show_id)
    episodes = adapters.get(adapter_name).get_episodes(channel_id)
    return Selection(name, description, choices(episodes, k=k))
