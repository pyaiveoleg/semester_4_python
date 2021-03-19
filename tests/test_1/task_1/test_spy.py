import unittest

from control_works.test_1.task_1 import spy, print_usage_statistics


class CacheTest(unittest.TestCase):
    def test_one_launch(self):
        @spy
        def test_func(num):
            print(num)

        test_func(30)
        time, parameters = next(print_usage_statistics(test_func))
        self.assertEqual(parameters, {"num": 30})

    def test_several_launches(self):
        @spy
        def test_func(num):
            print(num)

        test_func(30)
        stats = print_usage_statistics(test_func)
        time, parameters = next(stats)
        self.assertEqual(parameters, {"num": 30})

        test_func(2)
        time, parameters = next(stats)
        self.assertEqual(parameters, {"num": 2})

    def test_several_parameters(self):
        @spy
        def test_func(num1, num2):
            print(num1, num2)

        test_func(30, 31)
        time, parameters = next(print_usage_statistics(test_func))
        self.assertEqual(parameters, {"num1": 30, "num2": 31})

    def test_several_parameters_some_kwonly(self):
        @spy
        def test_func(num1, *, num2):
            print(num1, num2)

        test_func(30, num2=31)
        time, parameters = next(print_usage_statistics(test_func))
        self.assertEqual(parameters, {"num1": 30, "num2": 31})

    def test_several_parameters_some_posonly(self):
        @spy
        def test_func(num1, /, num2):
            print(num1, num2)

        test_func(30, num2=31)
        time, parameters = next(print_usage_statistics(test_func))
        self.assertEqual(parameters, {"num1": 30, "num2": 31})

    def test_without_spy(self):
        with self.assertRaises(Exception):

            def test_func(num1, /, num2):
                print(num1, num2)

            test_func(30, num2=31)
            time, parameters = next(print_usage_statistics(test_func))
            self.assertEqual(parameters, {"num1": 30, "num2": 31})
