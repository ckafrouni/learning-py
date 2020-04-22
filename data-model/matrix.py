class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])

    def __repr__(self):
        return f'{self.matrix}'

    def __str__(self):
        res = ''
        for i in range(self.row):
            line = ''
            for j in range(self.col):
                line += f'{self.matrix[i][j]:^3}'
            res+=f'\n|{line}|'
            
        return res