import time

from cell import Cell


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            self._cells.append([])
            for row in range(self._num_rows):
                x1 = self._x1 + (col * self._cell_size_x)
                x2 = x1 + self._cell_size_x
                y1 = self._y1 + (row * self._cell_size_y)
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, x2, y1, y2, self._win)
                self._cells[col].append(cell)
                
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        if self._win is not None:
            self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.1)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        max_col = len(self._cells) - 1
        max_row = len(self._cells[0]) - 1
        self._cells[max_col][max_row].has_bottom_wall = False
        self._draw_cell(max_col, max_row)