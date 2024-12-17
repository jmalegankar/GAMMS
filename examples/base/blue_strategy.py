import random
from gamms import sensors

def strategy(state):
    sensor_data = state['sensor']
    for (type, data) in sensor_data.values():
        if type == sensors.NEIGHBOR:
            choice = random.choice(range(len(data)))
            state['action'] = data[choice]
            break
    

def map_strategy(agent_config):
    strategies = {}
    for name in agent_config.keys():
        strategies[name] = strategy
    return strategies