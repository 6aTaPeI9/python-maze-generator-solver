import typing

class Ceil:
    def __init__(self, width: int, height: int, color: str):
        self.width = width
        self.height = height
        self.color = color


class Maze:
    """
        Класс-интерфейс для алгоритмов генерации лабиринта
    """
    def generate_maze(self) -> typing.Generator:
        """
            Метод генерации лабиринта, при измении каждой клеткий
            должен возвращаться генератор с данными о измененной клетке.
        """
        raise NotImplementedError('Метод generate_maze не реализован!')


def gen_maze_matrix(width: int, height: int) -> typing.List[width][height]:
    """
        Метод генерирует стандартную матрицу лабиринта,
        в котой клетки по умолчанию окружены стенами.
    """
    matrix = []
    for i in range(height):
        row = []
        for j in range(width):
            if j % 2 or i % 2: # четная позиция
                row.append(1)
            else: # нечетная позиция
                row.append(0)
        matrix.append(row)

    return matrix
