from gamms.VisualizationEngine import Color, Shape
from typing import Dict, Any


class RenderNode:
    def __init__(self, data: Dict[str, Any]):
        # self._x = x
        # self._y = y
        # self._layer = layer
        # self._color = color
        self._data = data

    @property
    def data(self):
        return self._data

    @property
    def x(self):
        return self._data['x']
    
    # @x.setter
    # def x(self, x):
    #     self._x = x

    @property
    def y(self):
        return self._data['y']
    
    # @y.setter
    # def y(self, y):
    #     self._y = y

    @property
    def layer(self):
        return self._data['layer']
    
    @property
    def color(self):
        return self._data['color']
    
    @property
    def shape(self) -> Shape:
        return self._data['shape']
    
    @property
    def drawer(self):
        return self._data['drawer']
    
    # @color.setter
    # def color(self, color):
    #     self._color = color