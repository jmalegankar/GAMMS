from config import location, graph_path
import gamms
import pickle
# Create a graph

G = gamms.osm.create_osm_graph(location)

# Save the graph
with open(graph_path, 'wb') as f:
    pickle.dump(G, f)