import gamms.AgentEngine.agent_engine as agent
import gamms.SensorEngine.sensor_engine as sensor
import gamms.GraphEngine.graph_engine as graph
import gamms.VisualizationEngine as visual
from gamms.context import Context
from enum import Enum

def create_context(
    vis_engine: Enum = visual.Engine.NO_VIS,
) -> Context:
    ctx = Context()
    if vis_engine == visual.Engine.NO_VIS:
        visual_engine = visual.no_engine.NoEngine(ctx)
    elif vis_engine == visual.Engine.PYGAME:
        visual_engine = visual.pygame_engine.PygameVisualizationEngine(ctx)
    else:
        raise NotImplementedError(f"Visualization engine {vis_engine} not implemented")
    
    graph_engine = _graph_engine.GraphEngine(ctx)
    agent_engine = _agent_engine.AgentEngine(ctx)
    sensor_engine = _sensor_engine.SensorEngine(ctx)
    ctx.agent_engine = agent_engine
    ctx.graph_engine = graph_engine
    ctx.visual_engine = visual_engine
    ctx.sensor_engine = sensor_engine
    ctx.set_alive()
    return ctx