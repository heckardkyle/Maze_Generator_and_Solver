import random
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
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)
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
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        max_col = len(self._cells) - 1
        max_row = len(self._cells[0]) - 1
        self._cells[max_col][max_row].has_bottom_wall = False
        self._draw_cell(max_col, max_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = self._check_neighboring_cells(i, j)
            if len(neighbors) <= 0:
                self._draw_cell(i, j)
                return
            next_cell_direction = neighbors[random.randrange(0, len(neighbors))]
            next_col, next_row = self._break_joining_wall(i, j, next_cell_direction)
            self._break_walls_r(next_col, next_row)

    def _check_neighboring_cells(self, i, j):
        neighbor_cells_to_visit = []
        #left_cell
        if i - 1 >= 0:
            if not self._cells[i-1][j].visited:
                neighbor_cells_to_visit.append("left")
        #right_cell
        if i + 1 < len(self._cells):
            if not self._cells[i+1][j].visited:
                neighbor_cells_to_visit.append("right")
        #top_cell
        if j - 1 >= 0:
            if not self._cells[i][j-1].visited:
                neighbor_cells_to_visit.append("top")
        #bottom_cell
        if j + 1 < len(self._cells[0]):
            if not self._cells[i][j+1].visited:
                neighbor_cells_to_visit.append("bottom")
        
        return neighbor_cells_to_visit
        
    def _break_joining_wall(self, i, j, next_cell_direction):
        if next_cell_direction == "left":
            self._cells[i][j].has_left_wall = False
            self._draw_cell(i, j)
            self._cells[i-1][j].has_right_wall = False
            self._draw_cell(i-1, j)
            return i-1, j
        
        if next_cell_direction == "right":
            self._cells[i][j].has_right_wall = False
            self._draw_cell(i, j)
            self._cells[i+1][j].has_left_wall = False
            self._draw_cell(i+1, j)
            return i+1, j
        
        if next_cell_direction == "top":
            self._cells[i][j].has_top_wall = False
            self._draw_cell(i, j)
            self._cells[i][j-1].has_bottom_wall = False
            self._draw_cell(i, j-1)
            return i, j-1
        
        if next_cell_direction == "bottom":
            self._cells[i][j].has_bottom_wall = False
            self._draw_cell(i, j)
            self._cells[i][j+1].has_top_wall = False
            self._draw_cell(i, j+1)
            return i, j+1
        
    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        
        # left
        if (
            i - 1 >= 0
            and self._cells[i][j].has_left_wall == False
            and self._cells[i-1][j].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j], False)
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        # right
        if (
            i + 1 < len(self._cells)
            and self._cells[i][j].has_right_wall == False
            and self._cells[i+1][j].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j], False)
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # top
        if (
            j - 1 >= 0
            and self._cells[i][j].has_top_wall == False
            and self._cells[i][j-1].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1], False)
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # bottom
        if (
            j + 1 < len(self._cells[0])
            and self._cells[i][j].has_bottom_wall == False
            and self._cells[i][j+1].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1], False)
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False

