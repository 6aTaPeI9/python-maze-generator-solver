from maze_generators import maze_matrix


class RecursiveBacktracker(maze_matrix.Maze):
    def __init__(self, width, heigth):
        self.title = 'Recursive Backtracker'
        self.width = width
        self.heigth = heigth
        self.matrix = maze_matrix.gen_maze_matrix(self.width, self.heigth)

    def generate_maze(self):
        pass