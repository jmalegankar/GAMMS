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


# pos = {node: (data['x'], data['y']) for node, data in G.nodes(data=True)}

# plt.figure(figsize=(12, 12))
# nx.draw(G, pos, node_size=10, node_color='blue', edge_color='gray', alpha=0.7, arrows=True, with_labels=False)

# plt.title('OSM Network Graph')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.show()

# fig, ax = plt.subplots(figsize=(12, 12))

# Extract node positions
# pos = {node: (data['x'], data['y']) for node, data in G.nodes(data=True)}

# Draw nodes
# nx.draw_networkx_nodes(G, pos, node_size=10, node_color='blue', ax=ax)

# # Prepare edge lines
# edge_lines = []
# for u, v, data in G.edges(data=True):
#     if 'linestring' in data:
#         # If a LineString geometry is present, use its coordinates
#         line = data['linestring']
#         x, y = line.xy
#         edge_lines.append(list(zip(x, y)))
#     else:
#         # Fallback to straight line if no geometry is provided
#         x1, y1 = pos[u]
#         x2, y2 = pos[v]
#         edge_lines.append([(x1, y1), (x2, y2)])

# # Create a LineCollection from the edge lines
# lc = LineCollection(edge_lines, colors='gray', linewidths=1, alpha=0.7)
# ax.add_collection(lc)

# # Set plot titles and labels
# ax.set_title('OSM Network Graph with LineString Geometries')

# plt.show()


# graph_egine.load(graph_path)
# graph_egine.graph.visualize()