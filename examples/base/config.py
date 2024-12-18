# The file describes the configuration for the game
import gamms


# Visualization
vis_engine = gamms.visual.Engine.NO_VIS

# The path to the graph file
location = "West Point, New York, USA"
graph_path = 'graph.npz'

# Sensor configuration
sensor_config = {
    'neigh_0': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_1': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_2': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_3': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_4': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_5': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_6': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_7': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_8': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'neigh_9': {
        'type': gamms.sensors.NEIGHBOR,
    },
    'map': {
        'type': gamms.sensors.MAP,
    },
    'agent': {
        'type': gamms.sensors.AGENT,
    }
}

# The configuration of the agents
agent_config = {
    'agent_0': {
        'meta': {'team': 0},
        'sensors': ['neigh_0', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_1': {
        'meta': {'team': 0},
        'sensors': ['neigh_1', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_2': {
        'meta': {'team': 0},
        'sensors': ['neigh_2', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_3': {
        'meta': {'team': 0},
        'sensors': ['neigh_3', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_4': {
        'meta': {'team': 0},
        'sensors': ['neigh_4', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_5': {
        'meta': {'team': 1},
        'sensors': ['neigh_5', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_6': {
        'meta': {'team': 1},
        'sensors': ['neigh_6', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_7': {
        'meta': {'team': 1},
        'sensors': ['neigh_7', 'map', 'agent'],
        'start_node_id': 0
    },
    
    'agent_8': {
        'meta': {'team': 1},
        'sensors': ['neigh_8', 'map', 'agent'],
        'start_node_id': 0
    },
    'agent_9': {
        'meta': {'team': 1},
        'sensors': ['neigh_9', 'map', 'agent'],
        'start_node_id': 0
    }
}

# # Visualization configuration
# graph_vis_config = {
#     'node_shape': gamms.visual.shapes.Circle,
#     'node_size': 500,
#     'node_color': gamms.visual.colors.LightBlue,
#     'edge_color': gamms.visual.colors.Black,
#     'width': 2,
#     'with_labels': True,
#     'pos': None
# }

# # Visualization configuration for the agents
# agent_vis_config = {
#     'agent_0': {
#         'color': 'blue',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_1': {
#         'color': 'blue',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_2': {
#         'color': 'blue',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_3': {
#         'color': 'blue',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_4': {
#         'color': 'blue',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_5': {
#         'color': 'red',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_6': {
#         'color': 'red',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_7': {
#         'color': 'red',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_8': {
#         'color': 'red',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     },
#     'agent_9': {
#         'color': 'red',
#         'size': 500,
#         'shape': gamms.visual.shapes.Triangle,
#     }
# }