

from line import Line
from point import Point


class Cell():
    def __init__(self, x1, x2, y1, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
        self.visited = False

    def draw(self):
        if self.has_left_wall == True:
            self.draw_wall(self._x1, self._x1, self._y1, self._y2, "black")
        else:
            self.draw_wall(self._x1, self._x1, self._y1, self._y2, "#d9d9d9")
        if self.has_right_wall == True:
            self.draw_wall(self._x2, self._x2, self._y1, self._y2, "black")
        else:
            self.draw_wall(self._x2, self._x2, self._y1, self._y2, "#d9d9d9")
        if self.has_top_wall == True:
            self.draw_wall(self._x1, self._x2, self._y1, self._y1, "black")
        else:
            self.draw_wall(self._x1, self._x2, self._y1, self._y1, "#d9d9d9")
        if self.has_bottom_wall == True:
            self.draw_wall(self._x1, self._x2, self._y2, self._y2, "black")
        else:
            self.draw_wall(self._x1, self._x2, self._y2, self._y2, "#d9d9d9")

    def draw_wall(self, x1, x2, y1, y2, fill_color):
        point_1 = Point(x1, y1)
        point_2 = Point(x2, y2)
        line = Line(point_1, point_2)
        if self._win is not None:
            self._win.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            fill_color = "red"
        else:
            fill_color = "gray"
        point_1 = Point((self._x1+self._x2)/2, (self._y1+self._y2)/2)
        point_2 = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        line = Line(point_1, point_2)
        if self._win is not None:
            self._win.draw_line(line, fill_color)
