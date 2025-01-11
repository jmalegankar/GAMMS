from gamms.VisualizationEngine import Color


class RenderNode:
    def __init__(self, x: float, y: float, layer: int = 0, color: tuple[int, int, int] = Color.Black):
        self._x = x
        self._y = y
        self._layer = layer
        self._color = color

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y

    @property
    def layer(self):
        return self._layer
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color