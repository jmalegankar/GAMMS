from typing import Callable
from abc import ABC, abstractmethod

class IVisualizationEngine(ABC):
    """
    The abstract interface for the visualization engine.
    """

    tick_callback: Callable[[float], None]
    """
    This will be called every tick of the game loop. You can use it for tick callback for other systems.

    Args:
        delta_time (float): The time in seconds since the last tick.
    """

    will_quit: bool
    """
    This will be set to True if the user tries to quit the game.
    """

    def __init__(self, tick_callback: Callable[[float], None]):
        super().__init__()

        self.tick_callback: Callable[[float], None] = tick_callback
        self.will_quit: bool = False

    def run_game_loop(self):
        """
        This is a basic game loop, can override in implementation.
        """
        while not self.will_quit:
            self.handle_input()
            self.handle_tick()
            self.handle_render()

        self.cleanup()

    @abstractmethod
    def handle_input(self):
        """
        This will be called every tick of the game loop, used to handle all input.
        """
        pass

    @abstractmethod
    def handle_tick(self):
        """
        This should handle all internal logic of visualization engine, as well as call the tick_callback.
        """
        pass

    @abstractmethod
    def handle_render(self):
        """
        This will be called every tick of the game loop, used to handle all rendering.
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        This will be called when the game loop exits. It should be used to clean up any resources that were used during the game loop.
        """
        pass