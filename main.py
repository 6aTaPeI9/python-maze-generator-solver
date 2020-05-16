import sys
import math
import time

from QMazeWidget import QMazeVisualizer
from maze_generators import maze_matrix
from PyQt5.QtWidgets import (QWidget, QMainWindow, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QGridLayout, QPushButton, QSlider, QLabel, QCheckBox, QApplication)
from PyQt5.QtCore import QObject, Qt, pyqtSignal, pyqtSlot, QThread, QTimer
from PyQt5.QtGui import QPainter, QFont, QColor, QPen, QPalette

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mazes = []

        self.setMinimumSize(300, 300)
        self.setWindowTitle('Maze alghoritms')
        self.InitWindow()
        self.timer.start()
        self.show()


    def InitWindow(self):
        """
            Метод инициализации основных компонентов основного экрана
        """
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.redraw_event)

        q_maze_grid = QGridLayout()
        q_maze_grid.setSpacing(0)
        q_maze_grid.addWidget(QWidget())

        row, col = 0, 0
        for i in range(1):
            maze = QMazeVisualizer(maze_matrix.Maze(50, 50))
            self.mazes.append(maze)

            if col >= 2:
                row += 1
                col = 0

            q_maze_grid.addWidget(maze, row, col)
            col += 1

        main_layout = QHBoxLayout()
        main_layout.addLayout(q_maze_grid)
        widget = QWidget()
        palette = widget.palette()
        widget.setAutoFillBackground(True)
        palette.setColor(widget.backgroundRole(), Qt.black)
        widget.setPalette(palette)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def redraw_event(self):
        for q_maze in self.mazes:
            q_maze.next.__next__()
            q_maze.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())