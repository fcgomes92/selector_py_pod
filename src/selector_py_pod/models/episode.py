class Episode:
    def __init__(self, id, title, link, thumbnail) -> None:
        self.id = id
        self.title = title
        self.link = link
        self.thumbnail = thumbnail

    def serialize(self) -> dict:
        return self.__dict__
