from abc import ABC, abstractmethod
from typing import Any, List
from enum import Enum

class IPathLike(ABC):
    pass

class IStore(ABC):
    def __init__(self, name: str, store_type: IStoreType, path: IPathLike):
        self.name = name 
        self.store_type = store_type
        self.path = path
        
    @abstractmethod
    def save(self, obj: Any) -> None:
        pass

    @abstractmethod
    def load(self) -> Any:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

class IMemoryEngine(ABC):
    @abstractmethod
    def create_store(self, store_type: Enum, name: str, path: IPathLike) -> IStore:
        pass

    @abstractmethod
    def list_stores(self) -> List[str]:
        pass

    @abstractmethod
    def load_store(self, name: str) -> IStore:
        pass