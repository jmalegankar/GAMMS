from gamms.typing import IContext
from gamms.typing.agent_engine import IAgent, IAgentEngine

from typing import Callable, Dict, Any, Optional, List

class Agent(IAgent):
    def __init__(self, graph, name, start_node_id, **kwargs):
        """Initialize the agent at a specific node with access to the graph and set the color."""
        self.graph = graph
        self.name = name
        self.sensor_list = {}
        self.prev_node_id = start_node_id
        self.current_node_id = start_node_id
        self.strategy: Optional[Callable[[Dict[str, Any]], None]] = None
        self._state = {}
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def register_sensor(self, name, sensor):
        self.sensor_list[name] = sensor
    

    def register_strategy(self, strategy):
        self.strategy = strategy
        
    def step(self):
        if self.strategy is None:
            raise AttributeError("Strategy is not set.")
        
        state = self.get_state()
        self.strategy(state)
        self.set_state()
        print(f"Moved to node {self.current_node_id}")


    def get_state(self) -> dict:
        for sensor in self.sensor_list.values():
            sensor.sense(self.current_node_id)

        state = {'curr_pos': self.current_node_id}
        state['sensor'] = {k:(sensor.type, sensor.data) for k, sensor in self.sensor_list.items()}
        self._state = state
        return self._state
    
    def set_state(self):
        self.prev_node_id = self.current_node_id
        self.current_node_id = self._state['action']


class AgentEngine(IAgentEngine):
    def __init__(self, ctx: IContext):
        self.ctx = ctx
        self.agents: List[IAgent] = []

    def create_iter(self):
        return self.agents.__iter__()
    
    def create_agent(self, name, **kwargs):
        start_node_id = kwargs.pop('start_node_id')
        agent = Agent(self.ctx.graph, name, start_node_id, **kwargs)
        for sensor in kwargs['sensors']:
            agent.register_sensor(sensor, self.ctx.sensor.get_sensor(sensor))
        self.agents.append(agent)
        return agent
    
    def terminate(self):
        return
    
    def get_agent(self, name) -> IAgent:
        for agent in self.agents:
            if agent.name == name:
                return agent
        else:
            raise ValueError(f"Agent {name} not found.")