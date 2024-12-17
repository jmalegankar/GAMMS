from config import location, graph_path

import gamms
import gamms.osm

# Create a graph
# graph_egine = GraphEngine()
# graph_egine.create_graph(location)
# graph_egine.graph.visualize()
# graph_egine.graph.save(graph_path)

G = gamms.osm.create_osm_graph(location)

print(G.edges(data=True))

# graph_egine.load(graph_path)
# graph_egine.graph.visualize()