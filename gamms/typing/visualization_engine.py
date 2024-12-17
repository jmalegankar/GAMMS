from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple

class IVisualizationEngine(ABC):
    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def handle_tick(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass

    @abstractmethod
    def render_text(self, text:str, x:int, y:int, coord_space: Enum, color: Tuple[int, int, int]):
        pass

    @abstractmethod
    def render_circle(self, x:float, y:float, radius:float, color: Tuple[int, int, int]):
        pass

    @abstractmethod
    def render_rectangle(self, x:float, y:float, width:float, height:float, color: Tuple[int, int, int]):
        pass

    @abstractmethod
    def render_line(self, start_x:float, start_y:float, end_x:float, end_y:float, color: Tuple[int, int, int], width:int, isAA:bool):
        pass