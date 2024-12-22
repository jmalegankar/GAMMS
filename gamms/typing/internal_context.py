from abc import ABC, abstractmethod
from gamms.typing.compute_engine import IComputeEngine
from gamms.typing.memory_engine import IMemoryEngine
from gamms.typing.message_engine import IMessageEngine

class IInternalContext(ABC):
    @property
    @abstractmethod
    def compute(self) -> IComputeEngine:
        pass

    @property
    @abstractmethod
    def memory(self) -> IMemoryEngine:
        pass

    @property
    @abstractmethod
    def message(self) -> IMessageEngine:
        pass

    @abstractmethod
    def terminate(self):
        pass