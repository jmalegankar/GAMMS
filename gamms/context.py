from gamms.typing import (
    IAgentEngine,
    IGraphEngine,
    ISensorEngine,
    IVisualizationEngine,
    IInternalContext,
    IContext
)

from typing import  Optional

class Context(IContext):
    def __init__(
        self,
        internal_context: Optional[IInternalContext] = None,
        agent_engine: Optional[IAgentEngine] = None,
        sensor_engine: Optional[ISensorEngine] = None,
        visual_engine: Optional[IVisualizationEngine] = None,
        graph_engine: Optional[IGraphEngine] = None,
    ):
        self.internal_context = internal_context
        self.agent_engine = agent_engine
        self.sensor_engine = sensor_engine
        self.visual_engine = visual_engine
        self.graph_engine = graph_engine
        self._alive = False
    
    @property
    def agent(self) -> IAgentEngine:
        return self.agent_engine

    @property
    def graph(self) -> IGraphEngine:
        return self.graph_engine
    
    @property
    def sensor(self) -> ISensorEngine:
        return self.sensor_engine
    
    @property
    def visual(self) -> IVisualizationEngine:
        return self.visual_engine
    
    @property
    def ictx(self) -> IInternalContext:
        return self.internal_context
    
    def set_alive(self):
        self._alive = True
    
    def is_terminated(self):
        return not self._alive
    
    def terminate(self):
        if self._alive:
            self.internal_context.terminate()
            self.agent_engine.terminate()
            self.sensor_engine.terminate()
            self.graph_engine.terminate()
            self.visual_engine.terminate()
            self._alive = False