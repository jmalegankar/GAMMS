import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Any
from shapely.geometry import LineString
from gamms.typing.graph_engine import Node, OSMEdge, IGraph, IGraphEngine
from gamms.osm import create_osm_graph
import pickle


class Graph(IGraph):
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.edges: Dict[str, OSMEdge] = {}
    
    def get_edge(self, edge_id):
        return self.edges[edge_id]

    def get_edges(self):
        return self.edges
    
    def get_node(self, node_id):
        return self.nodes[node_id]

    def get_nodes(self):
        return self.nodes
    
    def add_node(self, node_data: Dict[str, Any]) -> None:
        if node_data['id'] in self.nodes:
            raise KeyError(f"Node {node_data['id']} already exists.")
        
        node = Node(id=node_data['id'], x=node_data['x'], y=node_data['y'])
        self.nodes[node_data['id']] = node
    
    def add_edge(self, edge_data: Dict[str, Any]) -> None:
        if edge_data['id'] in self.edges:
            raise KeyError(f"Edge {edge_data['id']} already exists.")
        
        edge = OSMEdge(
            id = edge_data['id'],
            source=edge_data['source'],
            target=edge_data['target'],
            length=edge_data['length'],
            linestring=edge_data.get('linestring', None)
        )
        self.edges[edge_data['id']] = edge

    def update_node(self, node_data: Dict[str, Any]) -> None:
    
        if node_data['id'] not in self.nodes:
            raise KeyError(f"Node {node_data['id']} does not exist.")
        
        node = self.nodes[node_data['id']]
        node.x = node_data.get('x', node.x)
        node.y = node_data.get('y', node.y)
    
    def update_edge(self, edge_data: Dict[str, Any]) -> None:

        if edge_data['id'] not in self.edges:
            raise KeyError(f"Edge {edge_data['id']} does not exist. Use add_edge to create it.")
        edge = self.edges[edge_data['id']]
        edge.source = edge_data.get('source', edge.source)
        edge.target = edge_data.get('target', edge.target)
        edge.length = edge_data.get('length', edge.length)
        edge.linestring = edge_data.get('linestring', edge.linestring)

    def remove_node(self, node_id: int) -> None:
        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist.")
        
        edges_to_remove = [key for key, edge in self.edges.items() if edge.source == node_id or edge.target == node_id]
        for key in edges_to_remove:
            del self.edges[key]
            print(f"Deleted edge {key} associated with node {node_id}")
        del self.nodes[node_id]

    def remove_edge(self, node_id) -> None:
        if node_id not in self.edges:
            raise KeyError(f"Edge {node_id} does not exist. Use add_edge to create it.")
        del self.edges[id]
    
    def attach_networkx_graph(self, G: nx.Graph) -> None:
        for node, data in G.nodes(data=True):
            node_data = {
                'id': node,
                'x': data.get('x', 0.0),
                'y': data.get('y', 0.0)
            }
            self.add_node(node_data)
            
        for u, v, data in G.edges(data=True):
            edge_data = {
                'id': data.get('id', -1),
                'source': u,
                'target': v,
                'length': data.get('length', 0.0),
                'linestring': data.get('linestring', None)
            }
            self.add_edge(edge_data)
            
    def visualize(self) -> None:
        """
        Visualizes the graph using matplotlib. Nodes are plotted as points and edges as lines or curves.
        """
        plt.figure(figsize=(10, 10))

        # Plot nodes
        for node in self.nodes.values():
            plt.scatter(node.x, node.y, c='blue', s=50, label='Node' if node.id == next(iter(self.nodes)) else "")
        
        # Plot edges
        for edge in self.edges.values():
            source_node = self.nodes[edge.source]
            target_node = self.nodes[edge.target]

            if edge.linestring:
                # Ensure that the first point in linestring matches the source node and the last point matches the target node
                linestring = [(source_node.x, source_node.y)] + edge.linestring[1:-1] + [(target_node.x, target_node.y)]
                
                # Plot curved edge
                x_values, y_values = zip(*linestring)
                plt.plot(x_values, y_values, 'k-', alpha=0.7, label='Curved Edge' if edge == next(iter(self.edges.values())) else "")
            else:
                # Plot straight edge between source and target nodes
                plt.plot([source_node.x, target_node.x], [source_node.y, target_node.y], 'k-', alpha=0.5, label='Edge' if edge == next(iter(self.edges.values())) else "")
        
        plt.title("Graph Visualization")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(False)
        plt.show()
    
    def save(self, path: str) -> None:
        """
        Saves the graph to a file.
        """
        pickle.dump({"nodes": self.nodes, "edges": self.edges}, open(path, 'wb'))
        print(f"Graph saved to {path}")

    def load(self, path: str) -> None:
        """
        Loads the graph from a file.
        """
        data = pickle.load(open(path, 'rb'))
        self.nodes = data['nodes']
        self.edges = data['edges']


class GraphEngine(IGraphEngine):
    def __init__(self, ctx = None):
        self.ctx = ctx
        self.graph = None
    
    def graph(self) -> Graph:
        return self.graph

    def create_graph(self, location: str, network_type: str = 'walk', resolution=100, tolerance=10) -> Graph:
        """
        Creates a Graph object from a geographic location using OSMnx.
        """
        print(f"Creating graph for location: {location} with network type: {network_type}")
        G = create_osm_graph(location, resolution=100, tolerance=10)
        self.graph = Graph()
        self.graph.attach_networkx_graph(G)
        print("Graph creation complete.")
        return self.graph

    def load(self, path: str) -> Graph:
        """
        Loads a graph from a file.
        """
        self.graph = Graph()
        self.graph.load(path)
        return self.graph
    
    def terminate(self):
        return