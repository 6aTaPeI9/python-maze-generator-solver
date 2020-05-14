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
        self.setMinimumSize(1000, 900)
        self.setWindowTitle('Maze alghoritms')
        self.InitWindow()
        self.show()


    def InitWindow(self):
        """
            Метод инициализации основных компонентов основного экрана
        """
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(0.1)
        self.timer.timeout.connect(self.redraw_event)

        main_layout = QHBoxLayout()
        maze = maze_matrix.Maze(300, 300)
        q_maze = QMazeVisualizer(maze)
        main_layout.addWidget(q_maze)
        widget = QWidget()
        palette = widget.palette()
        widget.setAutoFillBackground(True)
        palette.setColor(widget.backgroundRole(), Qt.black)
        widget.setPalette(palette)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def redraw_event(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())