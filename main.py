from Line import Line
from Point import Point
from Window import Window


def main():
    win = Window(800, 600)

    # test drawing lines #
    point_1 = Point(0,0)
    point_2 = Point(200,200)
    point_3 = Point(0,200)
    point_4 = Point(200,0)
    line_1 = Line(point_1, point_2)
    line_2 = Line(point_3, point_4)
    win.draw_line(line_1, "red")
    win.draw_line(line_2, "black")
    #############################

    win.wait_for_close()

if __name__ == "__main__":
    main()