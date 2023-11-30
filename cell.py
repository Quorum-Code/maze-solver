from tkinter import Tk, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
        )
        canvas.pack()


class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win

    def draw(self):
        if not self.__win:
            return

        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
                             "black" if self.has_left_wall else "white")
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
                             "black" if self.has_right_wall else "white")
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
                             "black" if self.has_top_wall else "white")
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),
                             "black" if self.has_bottom_wall else "white")

    def center_point(self) -> Point:
        avg_x = (self.__x1 + self.__x2) // 2
        avg_y = (self.__y1 + self.__y2) // 2
        return Point(avg_x, avg_y)

    def draw_move(self, to_cell, undo=False):
        this_point = self.center_point()
        that_point = to_cell.center_point()
        if self.__win:
            self.__win.draw_line(Line(this_point, that_point), "red" if not undo else "gray")
