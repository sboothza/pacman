from enum import Enum, Flag

WIDTH = 638  # 319  # width of our game window
HEIGHT = 660  # 330  # height of our game window
FPS = 30  # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SPEED = 5


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Orientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class KeyPress(Flag):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8

keypress = KeyPress.NONE