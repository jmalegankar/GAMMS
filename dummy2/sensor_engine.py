from graph_engine import Node
from typing import Enum


class SensorType(Enum):
    NEIGHBOR = 1
    MAP = 2
    AGENT = 3

class NeighborSensor():
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

class MapSensor():
    def __init__(self, id, nodes, edges):
        self.id = id
        self.nodes = nodes
        self.edges = edges
    
    def sense(self):
        return self.nodes, self.edges
    
    def update():
        return
    
#return pos, node_id of all agents
class AgentSensor():
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
    
class SensorEngine():
    def __init__(self, graph):
        self.graph = graph  
        self.sensors = []
    def create_sensor(self, id, type: SensorType):
        if type == SensorType.NEIGHBOR:
            return NeighborSensor(id, self.graph.nodes, self.graph.edges)
        elif type == SensorType.MAP:
            return MapSensor(id, self.graph.nodes, self.graph.edges)
        elif type == SensorType.AGENT:
            return AgentSensor()
        else:
            raise ValueError("Invalid sensor type")
        



