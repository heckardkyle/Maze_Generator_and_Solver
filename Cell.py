

from Line import Line
from Point import Point


class Cell():
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = window

    def draw(self):
        if self.has_left_wall == True:
            self.draw_wall(self.__x1, self.__x1, self.__y1, self.__y2)
        if self.has_right_wall == True:
            self.draw_wall(self.__x2, self.__x2, self.__y1, self.__y2)
        if self.has_top_wall == True:
            self.draw_wall(self.__x1, self.__x2, self.__y1, self.__y1)
        if self.has_bottom_wall == True:
            self.draw_wall(self.__x1, self.__x2, self.__y2, self.__y2)

    def draw_wall(self, x1, x2, y1, y2):
        point_1 = Point(x1, y1)
        point_2 = Point(x2, y2)
        line = Line(point_1, point_2)
        self.__win.draw_line(line, "black")