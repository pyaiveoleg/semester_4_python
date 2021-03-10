import unittest
from typing import Callable

from homeworks.homework_2.task_1.uncurry import uncurry_explicit
from homeworks.homework_2.task_1.curry import curry_explicit

from tests.homework_2.task_1.test_curry import (
    fun_with_no_argument,
    fun_with_several_arguments,
    fun_with_one_argument,
    fun_with_infinity_arguments,
)


fun_with_no_argument_curried = curry_explicit(fun_with_no_argument, 0)
fun_with_one_argument_curried = curry_explicit(fun_with_one_argument, 1)
fun_with_several_arguments_curried = curry_explicit(fun_with_several_arguments, 3)
fun_with_infinity_arguments_curried = curry_explicit(fun_with_infinity_arguments, 4)


class UncurryTest(unittest.TestCase):
    def test_zero_arguments(self):
        return self.assertEqual(uncurry_explicit(fun_with_no_argument_curried, 0)(), fun_with_no_argument())

    def test_one_argument(self):
        return self.assertEqual(uncurry_explicit(fun_with_one_argument_curried, 1)("str"), fun_with_one_argument("str"))

    def test_several_arguments(self):
        f2 = uncurry_explicit(fun_with_several_arguments_curried, 3)
        return self.assertEqual(f2(123, 456, 789), fun_with_several_arguments("123", "456", "789"))

    def test_infinity_arguments_arity4(self):
        return self.assertEqual(
            uncurry_explicit(fun_with_infinity_arguments_curried, 4)("1", "2", "3", "4"),
            fun_with_infinity_arguments("1", "2", "3", "4"),
        )

    # block of incorrect cases

    def test_negative_arity(self):
        with self.assertRaises(AssertionError):
            uncurry_explicit(fun_with_infinity_arguments_curried, -5)("1")

    def test_infinity_arguments_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            uncurry_explicit(fun_with_infinity_arguments_curried, 4)("1", "2", "3", "4", "5")

    def test_infinity_arguments_less_args_than_arity(self):
        with self.assertRaises(TypeError):
            uncurry_explicit(fun_with_infinity_arguments_curried, 4)("1", "2", "3", "4", "5")

    def test_several_arguments_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            uncurry_explicit(fun_with_several_arguments_curried, 3)("1", "2", "3", "5")

    def test_one_argument_less_args_than_arity(self):
        self.assertTrue(isinstance(uncurry_explicit(fun_with_one_argument_curried, 1), Callable))

    def test_one_argument_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            uncurry_explicit(fun_with_one_argument_curried, 1)("1", "2")

    def test_zero_arguments_more_args_than_arity(self):
        with self.assertRaises(TypeError):
            uncurry_explicit(fun_with_no_argument_curried, 0)("1", "2")
