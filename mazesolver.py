import time
import random
from tkinter import Tk, Canvas
from cell import *
from visuals import *


class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None):

        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.cells = []

        if seed:
            random.seed(seed)
        else:
            random.seed()

        self.__create_cells()
        self._break_entrance_and_exit()
        self._reset_cells_visited()

    def __create_cells(self):
        self.cells = []

        y = self.__y1
        for i in range(self.__num_rows):
            x = self.__x1
            curr_row = []
            for j in range(self.__num_cols):
                new_cell = Cell(x, y, x+self.__cell_size_x, y+self.__cell_size_y, self.__win)
                curr_row.append(new_cell)
                x += self.__cell_size_x
            self.cells.append(curr_row)
            y += self.__cell_size_y

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.__draw_cells(i, j)

    def __draw_cells(self, i, j):
        if self.__win and self.cells[i] and self.cells[i][j]:
            self.cells[i][j].draw()
            self.__animate()

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            neighbors = []
            if i+1 < self.__num_rows and not self.cells[i+1][j].visited:
                neighbors.append((i+1, j))
            if i-1 > 0 and not self.cells[i-1][j].visited:
                neighbors.append((i-1, j))
            if j+1 < self.__num_rows and not self.cells[i][j+1].visited:
                neighbors.append((i, j+1))
            if j-1 > 0 and not self.cells[i][j-1].visited:
                neighbors.append((i, j-1))

            if len(neighbors) == 0:
                self.cells[i][j].draw()
                return

            index = int(random.random() * len(neighbors))

            if neighbors[index][0] > i:
                self.cells[i][j].has_bottom_wall = False
                self.cells[neighbors[index][0]][neighbors[index][1]].has_top_wall = False
            if neighbors[index][0] < i:
                self.cells[i][j].has_top_wall = False
                self.cells[neighbors[index][0]][neighbors[index][1]].has_bottom_wall = False
            if neighbors[index][1] > j:
                self.cells[i][j].has_right_wall = False
                self.cells[neighbors[index][0]][neighbors[index][1]].has_left_wall = False
            if neighbors[index][1] < j:
                self.cells[i][j].has_left_wall = False
                self.cells[neighbors[index][0]][neighbors[index][1]].has_right_wall = False

            self.cells[i][j].draw()
            self.__animate()
            self._break_walls_r(neighbors[index][0], neighbors[index][1])

    def _break_entrance_and_exit(self):
        if self.cells[0][0]:
            self.cells[0][0].has_top_wall = False
            self.cells[0][0].draw()
        if self.cells[self.__num_rows-1][self.__num_cols-1]:
            self.cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
            self.cells[self.__num_rows - 1][self.__num_cols - 1].draw()

        self._break_walls_r(0, 0)

    def __animate(self):
        if self.__win:
            self.__win.redraw()
            time.sleep(0.025)

    def _reset_cells_visited(self):
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self.cells[i][j].visited = False

    def _solve_r(self, i, j):
        self.__animate()
        self.cells[i][j].visited = True
        if i == self.__num_rows-1 and j == self.__num_cols-1:
            return True

        if not self.cells[i][j].has_bottom_wall and i+1 < self.__num_rows and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i + 1][j], True)

        if not self.cells[i][j].has_top_wall and i-1 > 0 and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i - 1][j], True)

        if not self.cells[i][j].has_right_wall and j+1 < self.__num_cols and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        if not self.cells[i][j].has_left_wall and j-1 > 0 and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        return False

    def solve(self):
        return self._solve_r(0, 0)
