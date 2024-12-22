from abc import ABC, abstractmethod
from enum import Enum

class ITask(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
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
    def terminate(self) -> None:
        pass