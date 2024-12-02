from abc import ABC, abstractproperty
from gamms.typing.compute_engine import IComputeEngine
from gamms.typing.memory_engine import IMemoryEngine
from gamms.typing.message_engine import IMessageEngine

class IInternalContext(ABC):
    @abstractproperty
    def compute(self) -> IComputeEngine:
        pass

    @abstractproperty
    def memory(self) -> IMemoryEngine:
        pass

    @abstractproperty
    def message(self) -> IMessageEngine:
        pass