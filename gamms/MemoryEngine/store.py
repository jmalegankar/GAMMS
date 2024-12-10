from typing.memory_engine import IStore, IPathLike

class PathLike(IPathLike):
    def __init__(self, path: str):
        self.path = path


class Store(IStore):
    def __init__(self, path: IPathLike):
        self.path = path

    def save(self, obj):
        pass

    def load(self):
        pass

    def delete(self):
        pass