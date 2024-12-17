from gamms.typing.sensor_engine import SensorType, ISensor, ISensorEngine

class NeighborSensor(ISensor):
    def __init__(self, id, type, nodes, edges):
        self.id = id
        self.type = type
        self.nodes = nodes
        self.edges = edges
        self.data = []
    
    #sense
    def sense(self, node_id):
        nearest_neighbors = set()
        for edge in self.edges.values():
            if edge.source == node_id:
                nearest_neighbors.add(edge.target)
            elif edge.target == node_id:
                nearest_neighbors.add(edge.source)
        self.data = list(nearest_neighbors)
    
    def update(self, node_id):
        return 

class MapSensor(ISensor):
    def __init__(self, id, type, nodes, edges):
        self.id = id
        self.type = type
        self.nodes = nodes
        self.edges = edges
        self.data = ((), ())
    
    def sense(self, node_id):
        self.data = (self.nodes, self.edges)
    
    def update(self, node_id):
        return
    
#return pos, node_id of all agents
class AgentSensor(ISensor):
    def __init__(self, id, type, agents):
        self.id = id
        self.type = type
        self.agents = agents
        self.data = []
    
    #sense
    def sense(self, node_id):
        agent_data = []
        for agent in self.agents:
            agent_data.append((agent.name, agent.current_node_id))
        self.data = agent_data
    
    def update(self, node_id):
        return 
    
class SensorEngine(ISensorEngine):
    def __init__(self, ctx):
        self.ctx = ctx  
        self.sensors = {}
    def create_sensor(self, id, type: SensorType, **kwargs):
        if type == SensorType.NEIGHBOR:
            sensor = NeighborSensor(id, type, self.ctx.graph_engine.graph.nodes, self.ctx.graph_engine.graph.edges)
        elif type == SensorType.MAP:
            sensor = MapSensor(id, type, self.ctx.graph_engine.graph.nodes, self.ctx.graph_engine.graph.edges)
        elif type == SensorType.AGENT:
            sensor = AgentSensor(id, type, self.ctx.agent_engine.agents)
        else:
            raise ValueError("Invalid sensor type")
        self.sensors[id] = sensor
        return sensor
    
    def get_sensor(self, id):
        return self.sensors[id]


