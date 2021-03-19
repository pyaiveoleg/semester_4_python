import unittest

from control_works.test_1.task_2.takes import takes


class TestTakes(unittest.TestCase):
    def test_one_incorrect_parameter(self):
        with self.assertRaises(TypeError):

            @takes(str)
            def test_func(par):
                print(par)

            test_func(5)

    def test_one_correct_one_incorrect_parameter(self):
        with self.assertRaises(TypeError):

            @takes(str, int)
            def test_func(par1, par2):
                print(par1)

            test_func("5", "10")

    def test_two_correct_parameters(self):
        @takes(str, int)
        def test_func(par1, par2):
            return par1, par2

        result = test_func("5", 10)
        self.assertEqual(("5", 10), result)

    def test_one_kwarg(self):
        @takes(str, str, str)
        def test_func(par1, /, par2, *, par3):
            return par1

        result = test_func("5", par2="6", par3="7")
        self.assertEqual("5", result)

    def test_posonly_usual_kwonly(self):
        @takes(str, str, str)
        def test_func(par1, /, par2, *, par3):
            return par1

        result = test_func("5", par2="6", par3="7")
        self.assertEqual("5", result)

    def test_less_types_than_in_signature(self):
        @takes(str, str)
        def test_func(par1, /, par2, *, par3):
            return par3

        result = test_func("5", par2="6", par3="7")  # it actually relaunches
        result = test_func("5", par2="6", par3=7)
        self.assertEqual(7, result)
