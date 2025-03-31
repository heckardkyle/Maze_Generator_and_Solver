from Cell import Cell
from Line import Line
from Maze import Maze
from Point import Point
from Window import Window


def main():
    win = Window(800, 600)

    # test drawing lines #
    maze = Maze(10, 10, 5, 5, 50, 50, win)
    #############################

    win.wait_for_close()

if __name__ == "__main__":
    main()