class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [
            list(map(int, row_num_str.split()))
            for row_num_str in matrix_string.splitlines()]

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [num[index - 1] for num in self._matrix]

    def tolist(self):
        return self._matrix.copy()
