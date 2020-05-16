import typing
from PyQt5.QtCore import Qt

class Ceil:
    def __init__(self, row_pos: int, col_pos: int, wall: bool = False):
        self.row_pos = row_pos
        self.col_pos = col_pos
        self.wall = wall
        self.vizited = False


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
        self._matrix = gen_maze_matrix(self.height, self.width)

    def generate_maze(self) -> typing.Generator:
        """
            Метод генерации лабиринта, при измении каждой клеткий
            должен возвращаться генератор с данными о измененной клетке.
        """
        raise NotImplementedError('Метод generate_maze не реализован!')

    def __getitem__(self, index: tuple) -> Ceil:
        """
            Метод возвращает обьект клетки по ее позиции в матрице
        """
        return self._matrix[index[0]][index[1]]

    
    def remove_wall(self, first_ceil: Ceil, second_ceil: Ceil):
        """
            Метод убирает стену между двумя клетками
        """
        diff_h = (first_ceil.col_pos + second_ceil.col_pos) // 2
        diff_w = (first_ceil.row_pos + second_ceil.row_pos) // 2

        wall_ceil = self.__getitem__((diff_h, diff_w))
        wall_ceil.vizited = True
        wall_ceil.wall = False


    def get_neighbours(self, ceil: Ceil, vizited: bool = True) -> list:
        """
            Метод возвращает ближайшие соседние клетки для переданной.
        """
        neighbors = [
            (ceil.col_pos - 2, ceil.row_pos), # верх
            (ceil.col_pos + 2, ceil.row_pos), # низ
            (ceil.col_pos, ceil.row_pos - 2), # лево
            (ceil.col_pos, ceil.row_pos + 2) # право
        ]
        valid_neighbors = []
        for neighbor in neighbors:
            # Проверяем что сосед не находится где то за пределами матрицы
            if neighbor[0] < 0 or neighbor[0] >= self.height:
                continue

            if neighbor[1] < 0 or neighbor[1] >= self.width:
                continue

            if self.__getitem__(neighbor).vizited:
                continue

            valid_neighbors.append(self.__getitem__(neighbor))

        return valid_neighbors




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
                row.append(Ceil(j, i, True))
            else: # нечетная позиция
                row.append(Ceil(j, i, False))
        matrix.append(row)

    return matrix
