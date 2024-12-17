from gamms.typing.sensor_engine import SensorType, ISensor, ISensorEngine

class NeighborSensor(ISensor):
    def __init__(self, id, nodes, edges):
        self.id = id
        self.nodes = nodes
        self.edges = edges
    
    #sense
    def sense(self, node_id):
        nearest_neighbors = set()
        for edge in self.edges.values():
            if edge.source == node_id:
                nearest_neighbors.add(edge.target)
            elif edge.target == node_id:
                nearest_neighbors.add(edge.source)
        return list(nearest_neighbors)
    
    def update():
        return 

class MapSensor(ISensor):
    def __init__(self, id, nodes, edges):
        self.id = id
        self.nodes = nodes
        self.edges = edges
    
    def sense(self):
        return self.nodes, self.edges
    
    def update():
        return
    
#return pos, node_id of all agents
class AgentSensor(ISensor):
    def __init__(self, name, nodes, edges):
        self.name = name
        self.nodes = nodes
        self.edges = edges
    
    #sense
    def sense(self, team):
        team_nodes = set()
        for node in self.nodes.values():
            if node.team == team:
                team_nodes.add(node)
        return list(team_nodes)
    
    def update():
        return 
    
class SensorEngine(ISensorEngine):
    def __init__(self, ctx):
        self.ctx = ctx  
        self.sensors = {}
    def create_sensor(self, id, type: SensorType, **kwargs):
        if type == SensorType.NEIGHBOR:
            sensor = NeighborSensor(id, self.ctx.graph_engine.graph.nodes, self.ctx.graph_engine.graph.edges)
        elif type == SensorType.MAP:
            sensor = MapSensor(id, self.ctx.graph_engine.graph.nodes, self.ctx.graph_engine.graph.edges)
        elif type == SensorType.AGENT:
            sensor = AgentSensor(id, self.ctx.graph_engine.graph.nodes, self.ctx.graph_engine.graph.edges)
        else:
            raise ValueError("Invalid sensor type")
        self.sensors[id] = sensor
        return sensor
    
    def get_sensor(self, id):
        return self.sensors[id]


