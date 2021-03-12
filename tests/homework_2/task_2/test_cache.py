import unittest
from collections import OrderedDict

from homeworks.homework_2.task_2.cache import enable_cache


class CacheTest(unittest.TestCase):
    def test_negative_size(self):
        with self.assertRaises(AssertionError):

            @enable_cache(size=-1)
            def function(x, y):
                return x + y

    def test_zero_size(self):
        @enable_cache(size=0)
        def function(x, y):
            return x + y

        function(5, 6)
        self.assert_(len(function.cache) == 0)

    def test_one_launch(self):
        @enable_cache(size=1)
        def function(x, y):
            return x + y

        function(5, 6)
        self.assertEqual(function.cache, OrderedDict([((5, 6), 11)]))

    def test_two_launches_size_1(self):
        @enable_cache(size=1)
        def function(x, y):
            return x + y

        function(5, 6)
        function(6, 7)
        self.assertEqual(function.cache, OrderedDict([((6, 7), 13)]))

    def test_many_launches_big_size(self):
        @enable_cache(size=6)
        def function(x, y):
            return x + y

        function(5, 6)
        function(6, 7)
        function(8, 9)
        self.assertEqual(function.cache, OrderedDict([((5, 6), 11), ((6, 7), 13), ((8, 9), 17)]))

    def test_with_kwargs(self):
        @enable_cache(size=2)
        def function(x, y):
            return x + y

        function(x=5, y=6)
        function(6, 7)
        self.assertEqual(function.cache, OrderedDict([((("x", 5), ("y", 6)), 11), ((6, 7), 13)]))

    def test_with_mixed_args(self):
        @enable_cache(size=2)
        def function(x, y):
            return x + y

        function(x=5, y=6)
        function(6, y=7)
        self.assertEqual(function.cache, OrderedDict([((("x", 5), ("y", 6)), 11), ((6, ("y", 7)), 13)]))
