from selector_py_pod.models.episode import Episode


class Selection:
    episodes = []

    def __init__(self, name, description, episodes=[]) -> None:
        self.name = name
        self.description = description
        self.episodes = episodes

    def add_episode(self, episode: Episode) -> list[Episode]:
        self.episodes.append(episode)
        return self.episodes

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'episodes': list(map(lambda o: o.serialize(), self.episodes))
        }
