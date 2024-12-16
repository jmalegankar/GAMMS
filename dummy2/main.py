from graph_engine import *
from agent_engine import *
from sensor_engine import *


graph_engine = GraphEngine()

location = "West Point, New York, USA"
G = graph_engine.create_graph_from_location(location, network_type='walk')

sensor_engine = SensorEngine(G)
agent_engine = AgentEngine(G, sensor_engine)


#{Agent: Kwargs}
for i in range(5):
    agent = agent_engine.create_agent(start_node_id=i)
    for j in range(3):
        sensor = sensor_engine.create_sensor(type=SensorType.NEIGHBOR)
        agent.register_sensor(name=sensor.id, sensor=sensor)

