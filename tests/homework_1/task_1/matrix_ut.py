import unittest

from homeworks.homework_1.task_1.matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_transpose(self):
        matrix = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        )
        transposed = Matrix(
            [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
            ]
        )
        self.assertEqual(matrix.transpose(), transposed)

    def test_add(self):
        matrix_1 = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        )
        matrix_2 = Matrix(
            [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
            ]
        )
        right_answer = Matrix(
            [
                [2, 6, 10],
                [6, 10, 14],
                [10, 14, 18],
            ]
        )
        self.assertEqual(matrix_1 + matrix_2, right_answer)

    def test_add_one_different_dimension(self):
        matrix_1 = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        matrix_2 = Matrix(
            [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
            ]
        )
        with self.assertRaises(ValueError):
            matrix_1 + matrix_2

    def test_add_both_different_dimensions(self):
        matrix_1 = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        matrix_2 = Matrix(
            [
                [1, 4],
                [2, 5],
                [3, 6],
            ]
        )
        with self.assertRaises(ValueError):
            matrix_1 + matrix_2

    def test_mul_one_different_dimension(self):
        matrix_1 = Matrix(
            [
                [1.6, 2.4, 3.9],
                [4.2, 5.2, 6.1],
            ]
        )
        matrix_2 = Matrix(
            [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
            ]
        )
        with self.assertRaises(ValueError):
            matrix_1 * matrix_2

    def test_mul_both_different_dimensions(self):
        matrix_1 = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        matrix_2 = Matrix(
            [
                [1, 4, 7],
                [2, 5, 8]
            ]
        )
        with self.assertRaises(ValueError):
            matrix_1 * matrix_2

    def test_mul_float_matrices(self):
        matrix_1 = Matrix(
            [
                [1.13, 2.43, 3.11],
                [4.09, -5.4, 6.0],
            ]
        )
        matrix_2 = Matrix(
            [
                [0, 0],
                [0.4, 5.1],
                [3.5, -6.2],
            ]
        )
        right_answer = Matrix(
            [
                [11.857, -6.889],
                [18.84, -64.74]
            ]
        )

        self.assertEqual(matrix_1 * matrix_2, right_answer)
