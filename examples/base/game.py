import gamms
from config import (
    #vis_engine,
    graph_path,
    sensor_config,
    agent_config
    #graph_vis_config,
    #agent_vis_config,
)
from gamms.GraphEngine.graph_engine import GraphEngine
from gamms.SensorEngine.sensor_engine import SensorEngine
from gamms.AgentEngine.agent_engine import AgentEngine
# from blue_strategy import blue_strategy
ctx = gamms.Context()

ctx.graph_engine = GraphEngine()

# Load the graph
G = ctx.graph_engine.load(graph_path)
#G.visualize()
ctx.sensor_engine = SensorEngine(ctx)

# Create the sensors
for name, sensor in sensor_config.items():
    ctx.sensor.create_sensor(name, sensor['type'], **sensor.get('args', {}))

#print(ctx.sensor.sensors)
ctx.agent_engine = AgentEngine(ctx)

# Create the agents
for name, agent in agent_config.items():
    ctx.agent.create_agent(name, **agent)

#print(ctx.agent.agents)
for agent in ctx.agent.agents:
    agent.step()
# Create the strategies
# strategies = blue_strategy.map_strategy(
#     {name: val for name, val in agent_config.items() if val['meta']['team'] == 0}
# )
# strategies.update(red_strategy.map_strategy(
#     {name: val for name, val in agent_config.items() if val['meta']['team'] == 1}
# ))

# # Set the strategies
# for agent in ctx.agent.create_iter():
#     agent.register_strategy(strategies.get(agent.name, None))

# # Set visualization configurations
# ctx.visualize.graph_config(**graph_vis_config)

# # Set agent visualization configurations
# for name, config in agent_vis_config.items():
#     ctx.visualize.agent_config(name, **config)


# turn_count = 0
# # Rules for the game
# def rule_terminate(ctx):
#     if turn_count > 100:
#         ctx.terminate()
#         return True
#     return False

# def agent_reset(ctx):
#     blue_agent_pos = {}
#     red_agent_pos = {}
#     for agent in ctx.agent.create_iter():
#         if agent.meta['team'] == 0:
#             blue_agent_pos[agent.name] = agent.current_pos
#         else:
#             red_agent_pos[agent.name] = agent.current_pos
#     for blue_agent in blue_agent_pos:
#         for red_agent in red_agent_pos:
#             if blue_agent_pos[blue_agent] == red_agent_pos[red_agent]:
#                 ctx.agent.get_agent(red_agent).current_pos = ctx.graph.get_random_node()

# def valid_step(ctx):
#     for agent in ctx.agent.create_iter():
#         state = agent.get_state()
#         sensor_name = agent_config[agent.name]['sensors'][0]
#         if agent.current_pos not in state[sensor_name]:
#             agent.current_pos = agent.prev_pos


# # Run the game
# while not ctx.is_terminated():
#     turn_count += 1
#     for agent in ctx.agent.create_iter():
#         if agent.strategy is not None:
#             agent.step()
#         else:
#             ctx.human_input()
#     valid_step(ctx)
#     agent_reset(ctx)
#     ctx.visualize.update()
#     ctx.save_frame()
#     rule_terminate(ctx)