import gamms
from config import (
    vis_engine,
    graph_path,
    sensor_config,
    agent_config,
    graph_vis_config,
    agent_vis_config
)
import blue_strategy
import red_strategy

ctx = gamms.create_context(vis_engine=vis_engine)

# Load the graph
ctx.graph.load(graph_path)


# Create the sensors
for name, sensor in sensor_config.items():
    ctx.sensor.create_sensor(name, sensor['type'], **sensor.get('args', {}))


# Create the agents
for name, agent in agent_config.items():
    ctx.agent.create_agent(name, **agent)

# Create the strategies
strategies = {}
# strategies.update(blue_strategy.map_strategy(
#     {name: val for name, val in agent_config.items() if val['meta']['team'] == 0}
# ))
strategies.update(red_strategy.map_strategy(
    {name: val for name, val in agent_config.items() if val['meta']['team'] == 1}
))

# Set the strategies
for agent in ctx.agent.create_iter():
    agent.register_strategy(strategies.get(agent.name, None))

#  # Set visualization configurations
ctx.visual.set_graph_visual(**graph_vis_config)

# Set agent visualization configurations

for name, config in agent_vis_config.items():
    ctx.visual.set_agent_visual(name, **config)




# turn_count = 0
# # Rules for the game
# def rule_terminate(ctx):
#     if turn_count > 100:
#         ctx.terminate()
#         return True
#     return False

def agent_reset(ctx):
    blue_agent_pos = {}
    red_agent_pos = {}
    for agent in ctx.agent.create_iter():
        if agent.meta['team'] == 0:
            blue_agent_pos[agent.name] = agent.current_node_id
        else:
            red_agent_pos[agent.name] = agent.current_node_id
    for blue_agent in blue_agent_pos:
        for red_agent in red_agent_pos:
            if blue_agent_pos[blue_agent] == red_agent_pos[red_agent]:
                ctx.agent.get_agent(red_agent).current_node_id = 0

def valid_step(ctx):
    for agent in ctx.agent.create_iter():
        state = agent.get_state()
        sensor_name = agent_config[agent.name]['sensors'][0]
        if agent.current_node_id not in state[sensor_name]:
            agent.current_node_id = agent.prev_node_id


# Run the game
while not ctx.is_terminated():
    # turn_count += 1
    # when waiting for human input, we don't want to update the agent
    if ctx.visual.waiting_user_input:
        # still need to update the render
        ctx.visual.update()

        result = ctx.visual.input_option_result
        if result:
            agent = ctx.visual.current_waiting_agent
            state = agent.get_state()
            state['action'] = result
            agent.set_state()
            ctx.visual.end_handle_human_input()

        continue

    for agent in ctx.agent.create_iter():
        if agent.strategy is not None:
            agent.step()
        else:
            # tell visual to start waiting for human input
            ctx.visual.human_input(agent)

    #valid_step(ctx)
    #agent_reset(ctx)
    # break
    
    ctx.visual.update()

    # ctx.save_frame()
    # rule_terminate(ctx)