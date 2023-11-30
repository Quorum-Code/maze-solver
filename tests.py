import unittest
from mazesolver import *


class Tests(unittest.TestCase):
    def setUp(self):
        self.x_offset = 25
        self.y_offset = 25
        self.num_rows = 8
        self.num_cols = 8
        self.cell_size = 60

        self.maze = Maze(self.x_offset, self.y_offset, self.num_rows, self.num_cols, self.cell_size, self.cell_size)

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_reset_visted(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.assertEqual(self.maze.cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
