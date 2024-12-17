from abc import ABC, abstractmethod
from gamms.typing import IInternalContext, ISensorEngine, IVisualizationEngine, IAgentEngine, IGraphEngine

class IContext(ABC):
    @property
    @abstractmethod
    def ictx(self) -> IInternalContext:
        pass

    @property
    @abstractmethod
    def sensor(self) -> ISensorEngine:
        pass

    @property
    @abstractmethod
    def visualize(self) -> IVisualizationEngine:
        pass

    @property
    @abstractmethod
    def agent(self) -> IAgentEngine:
        pass

    @property
    @abstractmethod
    def graph(self) -> IGraphEngine:
        pass