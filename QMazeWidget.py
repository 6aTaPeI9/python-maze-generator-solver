from maze_generators import maze_matrix
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QColor


class QMazeVisualizer(QWidget):
    def __init__(self, maze: maze_matrix.Maze, title = 'test'):
        super().__init__()
        self.title = title
        self.maze = maze

    def paintEvent(self, event):
        """
            Событие перерисовки окна
        """
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):
        """
            Метод перерисовывющий виджет
        """
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.gray)
        qp.setBrush(Qt.white)

        parent_size = self.size()
        parent_w, parent_h = parent_size.width(), parent_size.height()

        # height_padding = (self.maze.height * 1) # оступ между клетками по ширине
        # width_padding = (self.maze.width * 1) # отступ между клетками по высотке

        bar_size = parent_w if parent_w < parent_h else parent_h
        min_bars_in_line = self.maze.width if self.maze.width > self.maze.height else self.maze.height

        bar_size = bar_size // min_bars_in_line

        x_center_scale = (parent_h - self.maze.width * bar_size) // 2
        y_center_scale = (parent_w - self.maze.height * bar_size) // 2
        print(x_center_scale, y_center_scale)
        for col in range(self.maze.height):
            for row in range(self.maze.width):
                ceil = self.maze.matrix[col][row]
                qp.setBrush(ceil.color)
                qp.drawRect(
                    row * bar_size + x_center_scale,
                    col * bar_size + y_center_scale,
                    bar_size,
                    bar_size
                )

        return

