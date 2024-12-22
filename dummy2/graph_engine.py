import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass
from shapely.geometry import LineString



@dataclass
#change name in future
class Node:
    id: int
    x: float
    y: float
    base: bool

@dataclass
class OSMEdge:
    source: int #Node ID
    target: int #Node ID
    length: float
    linestring: List[Tuple[float, float]] = None


class Graph:
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.edges: Dict[str, OSMEdge] = {}

    def add_node(self, node_data: Dict[str, Any]) -> None:
        node_id = node_data['id']
        if node_id in self.nodes:
            print(f"Node {node_id} already exists.")
            return
        node = Node(id=node_id, x=node_data['x'], y=node_data['y'], base=node_data['base'])
        self.nodes[node_id] = node
        # print(f"Added node: {node}")
    
    def add_edge(self, edge_data: Dict[str, Any]) -> None:
        source = edge_data['source']
        target = edge_data['target']
        key = f"{source}-{target}"
        if key in self.edges:
            print(f"Edge {key} already exists.")
            return
        
        # Extract the geometry if available
        linestring = None
        if 'geometry' in edge_data and isinstance(edge_data['geometry'], LineString):
            linestring = [(point[0], point[1]) for point in edge_data['geometry'].coords]
        
        edge = OSMEdge(
            source=source,
            target=target,
            length=edge_data['length'],
            linestring=linestring
        )
        self.edges[key] = edge


    def update_node(self, node_data: Dict[str, Any]) -> None:
        node_id = node_data['id']
        if node_id not in self.nodes:
            print(f"Node {node_id} does not exist.")
            return
        node = self.nodes[node_id]
        node.x = node_data.get('x', node.x)
        node.y = node_data.get('y', node.y)


    def update_edge(self, edge_data: Dict[str, Any]) -> None:
        source = edge_data['source']
        target = edge_data['target']
        key = f"{source}-{target}"
        if key not in self.edges:
            print(f"Edge {key} does not exist. Use add_edge to create it.")
            return
        self.edges[key].length = edge_data.get('length', self.edges[key].length)
        # print(f"Updated edge {key}: {self.edges[key]}")

    def delete_node(self, node_id: int) -> None:
        if node_id not in self.nodes:
            print(f"Node {node_id} does not exist.")
            return
        edges_to_remove = [key for key, edge in self.edges.items() if edge.source == node_id or edge.target == node_id]
        for key in edges_to_remove:
            del self.edges[key]
            print(f"Deleted edge {key} associated with node {node_id}")
        del self.nodes[node_id]

    def delete_edge(self, source: int, target: int) -> None:
        key = f"{source}-{target}"
        if key not in self.edges:
            print(f"Edge {key} does not exist.")
            return
        del self.edges[key]
    
    def attach_networkx_graph(self, G: nx.Graph) -> None:
        for node, data in G.nodes(data=True):
            node_data = {
                'id': node,
                'x': data.get('x', 0.0),
                'y': data.get('y', 0.0),
                'base': True
            }
            self.add_node(node_data)
        for u, v, data in G.edges(data=True):
            edge_data = {
                'source': u,
                'target': v,
                'length': data.get('length', 0.0),
                'geometry': data.get('geometry', None)
            }
            self.add_edge(edge_data)

    # Function to calculate the distance between two nodes using longitude. Returns in meters
    def LongitudeLength(self, lat1, lon1, lat2, lon2):
        # Haversine formula to calculate distance between two lat/lon points
        R = 6371 
        dlat = np.radians(lat2 - lat1)
        dlon = np.radians(lon2 - lon1)
        a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = R * c * 1000
        return distance

    def attach_networkx_unit_graph(self, G: nx.Graph) -> None:
        # Stores G's points
        base_nodes = []
        base_edges = []
        segment_length = 50

        # Generate G
        # =================================================
        for node, data in G.nodes(data=True):
            node_data = {
                'id': node,
                'x': data.get('x', 0.0),
                'y': data.get('y', 0.0),
                'base': True
            }
            base_nodes.append(node_data)

        for u, v, data in G.edges(data=True):
            edge_data = {
                'source': u,
                'target': v,
                'length': data.get('length', 0.0),
                'geometry': data.get('geometry', None)
            }
            base_edges.append(edge_data)
        # =================================================

        # Stores G' 
        updated_node_prime = base_nodes.copy()
        updated_edge_prime = []
        new_node_id = len(base_nodes)  

        # Generate G'
        # =================================================
        for edge_data in base_edges:
            u = edge_data['source']
            v = edge_data['target']

            node_u = next((node for node in base_nodes if node['id'] == u), None)
            node_v = next((node for node in base_nodes if node['id'] == v), None)
            
            if node_u is None or node_v is None:
                continue
            
            lat_1, lon_1 = node_u['y'], node_u['x']
            lat_2, lon_2 = node_v['y'], node_v['x']

            total_length = self.LongitudeLength(lat_1, lon_1, lat_2, lon_2)
            
            num_segments = round(total_length // segment_length)

            if num_segments <= 1:
                updated_edge_prime.append(edge_data)
                continue

            last_node_id = u 
            for i in range(1, num_segments): 
                lat_new = lat_1 + (i / num_segments) * (lat_2 - lat_1)
                lon_new = lon_1 + (i / num_segments) * (lon_2 - lon_1)

                new_node_id += 1
                new_node = {
                    'id': new_node_id,
                    'x': lon_new,
                    'y': lat_new,
                    'base': False
                }
                updated_node_prime.append(new_node)

                updated_edge_prime.append({
                    'source': last_node_id,
                    'target': new_node_id,
                    'length': segment_length,
                    'geometry': LineString([(lon_1, lat_1), (lon_new, lat_new)])
                })

                last_node_id = new_node_id

            updated_edge_prime.append({
                'source': last_node_id,
                'target': v,
                'length': segment_length,
                'geometry': LineString([(lon_1, lat_1), (lon_2, lat_2)])
            })
        # =================================================

        for node in updated_node_prime:
            self.add_node(node)
        for edge in updated_edge_prime:
            self.add_edge(edge)
    
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


class GraphEngine:
    def __init__(self):
        pass


    def create_graph_from_location(self, location: str, network_type: str = 'walk') -> Graph:
        """
        Creates a Graph object from a geographic location using OSMnx.
        """
        print(f"Creating graph for location: {location} with network type: {network_type}")
        G = ox.graph_from_place(location, network_type=network_type)
        graph = Graph()
        graph.attach_networkx_unit_graph(G)
        print("Graph creation complete.")
        return graph


if __name__ == "__main__":
    engine = GraphEngine()
    location = "West Point, New York, USA"
    graph = engine.create_graph_from_location(location, network_type='walk')

    graph.visualize()
    # Example operations
    print("\n--- Adding a new node ---")
    graph.add_node({'id': 999999, 'x': -73.998, 'y': 41.394})

    print("\n--- Adding a new edge ---")
    graph.add_edge({'source': 999999, 'target': list(graph.nodes.keys())[0], 'length': 100.0})

    print("\n--- Updating a node ---")
    graph.update_node({'id': 999999, 'x': -73.999, 'y': 41.395})

    print("\n--- Deleting an edge ---")
    if graph.edges:
        first_edge = next(iter(graph.edges.values()))
        graph.delete_edge(first_edge.source, first_edge.target)

    print("\n--- Deleting a node ---")
    graph.delete_node(999999)