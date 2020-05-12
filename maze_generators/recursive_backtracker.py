from maze_generators import maze_matrix


class RecursiveBacktracker(maze_matrix.Maze):
    def __init__(self, width, height):
        self.title = 'Recursive Backtracker'
        self.width = width
        self.height = height
        self.matrix = maze_matrix.gen_maze_matrix(self.width, self.height)

    def generate_maze(self):
        pass