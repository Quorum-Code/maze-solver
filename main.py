from mazesolver import *


def main():
    win = Window(800, 600)
    maze = Maze(25, 25, 8, 8, 60, 60, win, 0)
    maze.solve()

    win.wait_for_close()


main()
