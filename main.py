from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window


def main():
    win = Window(800, 600)

    # test drawing lines #
    maze = Maze(10, 10, 10, 10, 50, 50, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    #############################

    win.wait_for_close()

if __name__ == "__main__":
    main()