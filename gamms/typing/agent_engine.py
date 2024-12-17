from abc import ABC, abstractmethod
from typing import Any


#CAN CHANGE
class IAgent(ABC):
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
    def create_agent(self, start_node_id):
        pass