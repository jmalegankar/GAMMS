from abc import ABC, abstractmethod

class IAgent(ABC):
    name: str

    @abstractmethod
    def step(self):
        pass
    @abstractmethod
    def get_state(self):
        pass
    @abstractmethod
    def set_state(self, state):
        pass

    @abstractmethod
    def register_sensor(self, name, sensor):
        pass

    @abstractmethod
    def register_strategy(self, strategy):
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
    def get_agent(self, name: str) -> IAgent:
        pass