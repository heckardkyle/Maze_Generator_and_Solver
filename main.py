from Cell import Cell
from Line import Line
from Point import Point
from Window import Window


def main():
    win = Window(800, 600)

    # test drawing lines #
    cell_1 = Cell(200, 400, 200, 400, win)
    cell_2 = Cell(500, 600, 500, 600, win)
    cell_1.draw()
    cell_2.draw()
    #############################

    win.wait_for_close()

if __name__ == "__main__":
    main()