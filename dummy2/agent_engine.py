import random

class Agent:
    def __init__(self, graph, start_node_id):
        """Initialize the agent at a specific node with access to the graph and set the color."""
        self.graph = graph
        self.sensor_list = {}
        self.prev_node_id = None
        self.current_node_id = start_node_id
    
    def register_sensor(self, name, sensor):
        self.sensor_list[name] = sensor

    def step(self, human=False):
        nodes_to_move = self.sensor.get_nearest_node(self.current_node_id)
        if human:
            print(f"Pick a node to move to from {self.current_node_id}:")
            for i, node_id in enumerate(nodes_to_move):
                print(f"{i}: {node_id}")
            choice = int(input())
        else:
            choice = random.choice(range(len(nodes_to_move)))
        self.current_node_id = nodes_to_move[choice]
        print(f"Moved to node {self.current_node_id}")


    def get_state(self) -> dict:
        """Get the current state of the agent."""
        return {"current_pos": self.current_node_id, "color": self.color}


class AgentEngine:
    def __init__(self, graph, sensor_engine):
        self.graph = graph
        self.sensor_engine = sensor_engine
        self.agents = []

    def create_iter(self):
        return self.agents.__iter__()
    
    def create_agent(self, start_node_id):
        agent = Agent(self.graph, start_node_id)
        self.agents.append(agent)
        return agent
    
