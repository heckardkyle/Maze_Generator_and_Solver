import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_reset_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        self.assertFalse(m1._cells[4][4].visited)
        self.assertFalse(m1._cells[0][0].visited)
        self.assertFalse(m1._cells[0][4].visited)
        self.assertFalse(m1._cells[4][0].visited)
        self.assertFalse(m1._cells[2][2].visited)

if __name__ == "__main__":
    unittest.main()