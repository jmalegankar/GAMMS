from enum import Enum

class Engine(Enum):
    NO_VIS = 0
    PYGAME = 1

class Color:
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    Yellow = (255, 255, 0)
    Cyan = (0, 255, 255)
    Magenta = (255, 0, 255)
    Gray = (169, 169, 169)
    LightGray = (211, 211, 211)
    DarkGray = (128, 128, 128)
    Brown = (210, 105, 30)
    Purple = (128, 0, 128)


class Space:
    World = 0
    Screen = 1
    Viewport = 2