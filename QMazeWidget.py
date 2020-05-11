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
            Метод перерисовывющий виджет
        """
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):
        pass