from enum import Enum
from typing import Union

from pygame.sprite import Sprite

from common import Direction, Orientation, KeyPress, SPEED


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add_x(self, x: int):
        self.x += x
        return self

    def add_y(self, y: int):
        self.y += y
        return self

    def point_is_node(self, current):
        return True if self.x == current.x and self.y == current.y else False


class Vector:
    def __init__(self, point: Point, direction: Direction):
        self.x = point.x
        self.y = point.y
        self.direction = direction


class Path:
    def __init__(self, node1: Point, node2: Point, name: str = ""):
        # flip the nodes if they're the wrong way around
        if node1.x <= node2.x and node1.y <= node2.y:
            self.node1 = node1
            self.node2 = node2
        else:
            self.node1 = node2
            self.node2 = node1
        self.orientation = Orientation.VERTICAL if node1.x == node2.x else Orientation.HORIZONTAL
        self.name = name

    def point_in_path(self, current: Point):
        if self.orientation == Orientation.VERTICAL and \
                self.node1.x == current.x and \
                self.node1.y <= current.y <= self.node2.y:
            return True
        elif self.orientation == Orientation.HORIZONTAL and \
                self.node1.y == current.y and \
                self.node1.x <= current.x <= self.node2.x:
            return True
        return False


class Map:
    def __init__(self):
        self.nodes = []
        self.paths = []

    def add_node(self, x: int, y: int) -> Point:
        node = Point(x, y)
        self.nodes.append(node)
        return node

    def add_path(self, node1: Point, node2: Point, name: str = "") -> Path:
        path = Path(node1, node2, name)
        self.paths.append(path)
        return path

    def find_node(self, current: Point) -> Union[Point, None]:
        found = [node for node in self.nodes if node.point_is_node(current)]
        if found is not None and len(found) > 0:
            return found[0]
        return None

    def find_path(self, current: Point) -> Union[Path, None]:
        """won't work on endpoints, only in the middle"""
        found = [path for path in self.paths if path.point_in_path(current)]
        if found is not None and len(found) > 0:
            return found[0]
        return None

    def move(self, current: Point, keypress: KeyPress) -> Point:
        """returns x,y of result"""

        # is node?
        node = self.find_node(current)
        if node is not None:
            # handle node
            # node is junction - track next path
            # find all paths
            paths = [p for p in self.paths if p.point_in_path(node)]
            for path in paths:
                if path.orientation == Orientation.HORIZONTAL:
                    if path.node1 == node and KeyPress.RIGHT in keypress:
                        return current.add_x(SPEED)
                    elif path.node2 == node and KeyPress.LEFT in keypress:
                        return current.add_x(-SPEED)
                else:
                    if path.node1 == node and KeyPress.UP in keypress:
                        return current.add_y(-SPEED)
                    elif path.node2 == node and KeyPress.DOWN in keypress:
                        return current.add_y(SPEED)

            return current

        else:  # must be path
            path = self.find_path(current)
            if path is None:
                return current  # something weird happened - return the same coords
            # handle path
            if path.orientation == Orientation.HORIZONTAL:
                if keypress == KeyPress.LEFT:
                    return current.add_x(-SPEED)
                elif keypress == KeyPress.RIGHT:
                    return current.add_x(SPEED)
            else:
                if keypress == KeyPress.UP:
                    return current.add_y(-SPEED)
                elif keypress == KeyPress.DOWN:
                    return current.add_y(SPEED)

        return current

    # def get_paths_for_node(self):


map = Map()
