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
        height_padding = (self.maze.height * 1) # оступ между клетками по ширине
        width_padding = (self.maze.width * 1) # отступ между клетками по высотке
        bar_width = (parent_size.width() - width_padding) // self.maze.width # масштабированная ширина клетки
        bar_height = (parent_size.height() - height_padding) // self.maze.height # масштабированная высота клетки

        for col in range(self.maze.height):
            for row in range(self.maze.width):
                ceil = self.maze.matrix[col][row]
                qp.setBrush(ceil.color)
                qp.drawRect(
                    row * bar_width,
                    col * bar_height,
                    bar_width,
                    bar_height
                )

        return

