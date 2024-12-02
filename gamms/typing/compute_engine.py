from abc import ABC, abstractmethod, abstractproperty
from enum import Enum

class ITask(ABC):
    @abstractproperty
    def id(self) -> str:
        pass

    @abstractproperty
    def status(self) -> Enum:
        pass

    @abstractmethod
    def run(self) -> None:
        pass


class IComputeEngine(ABC):
    @abstractmethod
    def submit(self, task: ITask) -> None:
        pass

    @abstractmethod
    def wait(self, task: ITask) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass