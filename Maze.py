import time

from Cell import Cell


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()

    def __create_cells(self):
        self.__cells = []
        for col in range(self.__num_cols):
            self.__cells.append([])
            for row in range(self.__num_rows):
                x1 = self.__x1 + (col * self.__cell_size_x)
                x2 = x1 + self.__cell_size_x
                y1 = self.__y1 + (row * self.__cell_size_y)
                y2 = y1 + self.__cell_size_y
                cell = Cell(x1, x2, y1, y2, self.__win)
                self.__cells[col].append(cell)
                
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw()
        self.__animate()
    
    def __animate(self):
        self.__win.redraw()
        time.sleep(0.1)