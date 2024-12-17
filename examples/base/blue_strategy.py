
def map_strategy(agent_config):
    strategies = {}
    for name, val in agent_config.items():
        strategies[name] = blue_strategy.BlueStrategy(name, val)
    return strategies