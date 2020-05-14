import typing
from PyQt5.QtCore import Qt

class Ceil:
    def __init__(self, row_pos: int, col_pos: int, color: str):
        self.row_pos = row_pos
        self.col_pos = col_pos
        self.color = color


class Maze:
    """
        Класс-интерфейс для алгоритмов генерации лабиринта
    """
    height = int()
    width = int()
    matrix = list()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = gen_maze_matrix(self.width, self.height)

    def generate_maze(self) -> typing.Generator:
        """
            Метод генерации лабиринта, при измении каждой клеткий
            должен возвращаться генератор с данными о измененной клетке.
        """
        raise NotImplementedError('Метод generate_maze не реализован!')


def gen_maze_matrix(height: int, width: int) -> typing.List:
    """
        Метод генерирует стандартную матрицу лабиринта,
        в котой клетки по умолчанию окружены стенами.
    """
    matrix = []
    for i in range(height):
        row = []
        for j in range(width):
            if j % 2 or i % 2: # четная позиция
                row.append(Ceil(j, i, Qt.white))
            else: # нечетная позиция
                row.append(Ceil(j, i, Qt.red))
        matrix.append(row)

    return matrix
