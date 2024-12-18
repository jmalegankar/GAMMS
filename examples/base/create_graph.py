from config import location, graph_path

import gamms
import gamms.osm

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from shapely.geometry import LineString
from gamms.GraphEngine.graph_engine import GraphEngine
# Create a graph

graph_egine = GraphEngine()
graph_egine.create_graph(location)
graph_egine.graph.visualize()
# graph_egine.graph.save(graph_path)

# graph_egine.load(graph_path)
# graph_egine.graph.visualize()