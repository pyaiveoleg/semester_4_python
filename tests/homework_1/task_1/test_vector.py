import unittest

from homeworks.homework_1.task_1.vector import Vector


class VectorTest(unittest.TestCase):
    def test_zero_length(self):
        self.assertEqual(Vector([]).length(), 0)

    def test_int_length(self):
        self.assertEqual(Vector([3, 4]).length(), 5)

    def test_float_length(self):
        self.assertAlmostEqual(Vector([0.1, 4, 3.5]).length(), 5.316013544)

    def test_different_dimensions_scalar_product(self):
        with self.assertRaises(ValueError):
            Vector([1, 2]).scalar_product(Vector([1, 3, 4]))

    def test_int_scalar_product(self):
        self.assertEqual(Vector([2, 3]).scalar_product(Vector([1, 4])), 14)

    def test_float_scalar_product(self):
        first_v = Vector([3.5, 1.74, 0.896, 0.445])
        second_v = Vector([1, -2.97, -1.065, -3.29])
        self.assertAlmostEqual(first_v.scalar_product(second_v), -4.08609)

    def test_self_scalar_product(self):
        self.assertAlmostEqual(Vector([1, -2.97, -1.065]).scalar_product(Vector([1, -2.97, -1.065])), 10.955125)

    def test_different_dimensions_angle(self):
        with self.assertRaises(ValueError):
            Vector([1, 2]).angle(Vector([1, 3, 4]))

    def test_float_angle(self):
        first_v = Vector([3.5, 1.74, 0.896, 0.445])
        second_v = Vector([1, -2.97, -1.065, -3.29])
        self.assertAlmostEqual(first_v.angle(second_v), 102.53349294109442)

    def test_self_angle(self):
        self.assertAlmostEqual(Vector([1, -2.97, -1.065]).angle(Vector([1, -2.97, -1.065])), 0.0)
