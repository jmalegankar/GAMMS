from abc import ABC, abstractmethod
from typing import Any, List


#CAN CHANGE
class IAgent(ABC):
    @abstractmethod
    def step(self):
        pass
    @abstractmethod
    def get_state(self):
        pass
    @abstractmethod
    def get_action(self):
        pass
    @abstractmethod
    def set_state(self, state: Any):
        pass
    @abstractmethod
    def set_action(self, action: Any):
        pass
    @abstractmethod
    def get_reward(self):
        pass
    @abstractmethod
    def set_reward(self, reward: Any):
        pass
    @abstractmethod
    def get_done(self):
        pass
    @abstractmethod
    def set_done(self, done: Any):
        pass
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def set_info(self, info: Any):
        pass




class IAgentEngine(ABC):
    @abstractmethod
    def step_all_agents(self):
        pass
    @abstractmethod
    def get_all_states(self):
        pass