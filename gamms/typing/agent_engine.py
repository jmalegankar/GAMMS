from abc import ABC, abstractmethod
from typing import Union


#CAN CHANGE
class IAgent(ABC):
    name: Union[str, int]

    @abstractmethod
    def step(self):
        pass
    @abstractmethod
    def get_state(self):
        pass
    @abstractmethod
    def set_state(self, state):
        pass

class IAgentEngine(ABC):
    @abstractmethod
    def create_iter(self):
        pass
    
    @abstractmethod
    def create_agent(self, start_node_id: int, **kwargs):
        pass

    @abstractmethod
    def terminate(self):
        pass

    @abstractmethod
    def get_agent(self, name: Union[str, int]) -> IAgent:
        pass