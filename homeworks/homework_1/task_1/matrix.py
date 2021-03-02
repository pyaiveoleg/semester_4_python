from typing import List

from homeworks.homework_1.task_1.vector import Vector


class Matrix:
    __matrix: List[List[float]]
    __rows: int
    __columns: int

    def __init__(self, matrix: List[List[float]], eps=0.01):
        if len(matrix) != 0:
            row_length = len(matrix[0])
            for row in matrix:
                if len(row) != row_length:
                    raise ValueError("Rows in a matrix should be equal length")
        self.eps = eps
        self.__rows = len(matrix)
        self.__columns = len(matrix[0])
        self.__matrix = matrix

    def __eq__(self, other: "Matrix") -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented

        for i in range(self.__rows):
            for j in range(self.__columns):
                if (self.__matrix[i][j] - other.__matrix[i][j]) > self.eps:
                    return False
        return True

    def transpose(self) -> "Matrix":
        return Matrix(list(map(list, zip(*self.__matrix))))

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.__rows != other.__rows or self.__columns != other.__columns:
            raise ValueError("Both dimensions of matrices should be equal")
        return Matrix([[x + y for x, y in zip(self.__matrix[i], other.__matrix[i])] for i in range(self.__rows)])

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.__rows != other.__columns or self.__columns != other.__rows:
            raise ValueError("Both dimensions of matrices should be equal")
        return Matrix(
            [
                [
                    Vector(self.__matrix[i]).scalar_product(Vector(other.transpose().__matrix[j]))
                    for j in range(self.__rows)
                ]
                for i in range(other.__columns)
            ]
        )
