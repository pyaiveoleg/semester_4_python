import unittest
from typing import Callable

from homeworks.homework_2.task_1.curry import curry_explicit


def fun_with_no_argument():
    return "Я пока ничего не умею..."


def fun_with_one_argument(x: object):
    return "I'm taking 1 argument"


def fun_with_several_arguments(x: str, y: str, z: str):
    return f"<{x}, {y}, {z}>"


def fun_with_infinity_arguments(*args):
    return "".join(args)


class CurryTest(unittest.TestCase):
    def test_zero_arguments(self):
        return self.assertEqual(curry_explicit(fun_with_no_argument, 0)(), "Я пока ничего не умею...")

    def test_one_argument(self):
        return self.assertEqual(curry_explicit(fun_with_one_argument, 1)("str"), "I'm taking 1 argument")

    def test_several_arguments(self):
        f2 = curry_explicit(fun_with_several_arguments, 3)
        return self.assertEqual(f2(123)(456)(789), "<123, 456, 789>")

    def test_infinity_arguments_arity1(self):
        return self.assertEqual(curry_explicit(fun_with_infinity_arguments, 1)("1"), "1")

    def test_infinity_arguments_arity3(self):
        return self.assertEqual(curry_explicit(fun_with_infinity_arguments, 3)("1")("2")("3"), "123")

    # block of incorrect cases

    def test_negative_arity(self):
        with self.assertRaises(AssertionError):
            curry_explicit(fun_with_infinity_arguments, -5)("1")

    def test_infinity_arguments_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            curry_explicit(fun_with_infinity_arguments, 1)("1")("2")

    def test_infinity_arguments_less_args_than_arity(self):
        with self.assertRaises(TypeError):
            curry_explicit(fun_with_infinity_arguments, 1)("1")("2")

    def test_several_arguments_more_args_than_arity(self):
        with self.assertRaises(ValueError):
            curry_explicit(fun_with_several_arguments, 1)("1")("2")

    def test_several_arguments_less_args_than_arity(self):
        with self.assertRaises(ValueError):
            curry_explicit(fun_with_several_arguments, 1)("1")("2")

    def test_one_argument_less_args_than_arity(self):
        self.assert_(isinstance(curry_explicit(fun_with_one_argument, 1), Callable))

    def test_one_argument_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            curry_explicit(fun_with_one_argument, 1)("1")("2")

    def test_zero_arguments_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            curry_explicit(fun_with_no_argument, 0)("1")("2")
