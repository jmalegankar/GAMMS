import gamms.AgentEngine.agent_engine as _agent_engine
import gamms.SensorEngine.sensor_engine as _sensor_engine
import gamms.GraphEngine.graph_engine as _graph_engine
import gamms.VisualizationEngine as _visual_engine
from gamms.context import Context

import gamms.visual

from enum import Enum

def create_context(
    vis_engine: Enum = gamms.visual.Engine.NO_VIS,
) -> Context:
    ctx = Context()
    if vis_engine == gamms.visual.Engine.NO_VIS:
        visual_engine = None
    elif vis_engine == gamms.visual.Engine.PYGAME:
        raise NotImplementedError()
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


from gamms.typing.sensor_engine import SensorType as sensors