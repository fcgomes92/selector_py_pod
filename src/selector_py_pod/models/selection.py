class Selection:
    episodes = []

    def __init__(self, name, description, episodes) -> None:
        self.name = name
        self.description = description
        self.episodes = episodes

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'episodes': list(map(lambda o: o.serialize(), self.episodes))
        }
