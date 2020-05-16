import random

from queue import Queue
from maze_generators import maze_matrix
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QColor


class QMazeVisualizer(QWidget):
    def __init__(self, maze: maze_matrix.Maze, title = 'test'):
        super().__init__()
        self.title = title
        self.maze = maze
        self.next = self.generate_maze()
        self.cur_ceil = None


    def paintEvent(self, event):
        """
            Событие перерисовки окна
        """
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def draw_next_pos(self):
        """
            Метод отрисовывает следующее положение 
        """
        pass

    def generate_maze(self):
        """
            Метод выполняет генерацию лабиринта из исходной матрицы
        """
        ceils_queue = Queue()

        self.cur_ceil = self.maze[(0, 0)]
        self.cur_ceil.vizited = True
        yield

        ceils_queue.put(self.cur_ceil)
        while True:
            neighbors = self.maze.get_neighbours(self.cur_ceil)
            print(neighbors)

            if len(neighbors) > 0:
                ceils_queue.put(self.cur_ceil)
                next_ceil = neighbors[random.randint(0, len(neighbors) - 1)]
                self.maze.remove_wall(self.cur_ceil, next_ceil)

                self.cur_ceil = next_ceil
                self.cur_ceil.vizited = True
                yield
                continue
            elif not ceils_queue.empty():
                self.cur_ceil = ceils_queue.get()
                self.cur_ceil.vizited = True
                yield
                continue

            break

    def get_ceil_color(self, ceil):
        """
            Метод возвращает цвет для переданной клетки
        """
        if self.cur_ceil == ceil:
            return Qt.green
        else:
            if ceil.wall:
                return Qt.black
            else:
                return Qt.white


    def drawWidget(self, qp):
        """
            Метод перерисовывющий виджет
        """
        qp.setPen(Qt.NoPen)

        parent_size = self.size()
        parent_w, parent_h = parent_size.width(), parent_size.height()

        # height_padding = (self.maze.height * 1) # оступ между клетками по ширине
        # width_padding = (self.maze.width * 1) # отступ между клетками по высотке

        bar_size = parent_w if parent_w < parent_h else parent_h
        min_bars_in_line = self.maze.width if self.maze.width > self.maze.height else self.maze.height

        bar_size = bar_size // min_bars_in_line

        x_center_scale = (parent_w - self.maze.width * bar_size) // 2
        y_center_scale = (parent_h - self.maze.height * bar_size) // 2

        for col in range(self.maze.height):
            for row in range(self.maze.width):
                ceil = self.maze[(col, row)]

                qp.setBrush(self.get_ceil_color(ceil))

                qp.drawRect(
                    row * bar_size + x_center_scale,
                    col * bar_size + y_center_scale,
                    bar_size,
                    bar_size
                )

        return

