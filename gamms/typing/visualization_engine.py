from typing import Dict, Any
from abc import ABC, abstractmethod

class IVisualizationEngine(ABC):
    @abstractmethod
    def set_graph_visual(self, **kwargs):
        """
        Set the visual configuration of the graph.
        """
        pass

    @abstractmethod
    def set_agent_visual(self, agent_name: str, **kwargs):
        """
        Set the visual configuration of an agent.
        """
        pass

    @abstractmethod
    def simulate(self):
        """
        This is the main loop of the visualization engine. This should be called in a loop to update the visualization.
        """
        pass

    @abstractmethod
    def human_input(self, state: Dict[str, Any]):
        """
        This should be called to get the input from the human player.
        """
        pass

    @abstractmethod
    def terminate(self):
        """
        This will be called when the game loop exits. It should be used to clean up any resources that were used during the game loop.
        """
        pass