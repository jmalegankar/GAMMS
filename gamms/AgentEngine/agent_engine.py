import random
from gamms.typing import IContext
from gamms.typing.agent_engine import IAgent, IAgentEngine


class Agent(IAgent):
    def __init__(self, graph, name, start_node_id, team):
        """Initialize the agent at a specific node with access to the graph and set the color."""
        self.graph = graph
        self.name = name
        self.sensor_list = {}
        self.prev_node_id = None
        self.current_node_id = start_node_id
        self.strategy = None
        self.team = team

    
    def register_sensor(self, name, sensor):
        self.sensor_list[name] = sensor
    
    def register_strategy(self, name, strategy):
        pass

    def step(self):
        if not self.strategy:
            nodes_to_move = self.sensor_list[0](self.current_node_id)
            # give me nearest nodes 
            print(f"Pick a node to move to from {self.current_node_id}:")
            for i, node_id in enumerate(nodes_to_move):
                print(f"{i}: {node_id}")
            choice = int(input()) # whatver u waant to do
        else:
            choice = random.choice(range(len(nodes_to_move)))

        
        self.current_node_id = nodes_to_move[choice]
        print(f"Moved to node {self.current_node_id}")


    def get_state(self) -> dict:
        """Get the current state of the agent."""
        return {"current_pos": self.current_node_id, "color": self.color}

    def set_state(self, state):
        return 


class AgentEngine(IAgentEngine):
    def __init__(self, ctx: IContext):
        self.ctx = ctx
        self.agents = []

    def create_iter(self):
        return self.agents.__iter__()
    
    def create_agent(self, name, **kwargs):
        agent = Agent(self.ctx.graph, name, kwargs['start_node_id'], kwargs['meta']['team'])
        for sensor in kwargs['sensors']:
            agent.register_sensor(sensor, self.ctx.sensor.get_sensor(sensor))
        self.agents.append(agent)
        return agent