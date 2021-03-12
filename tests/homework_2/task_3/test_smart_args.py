import unittest
from typing import Any

from homeworks.homework_2.task_3.smart_args import smart_args, Isolated, Evaluated


class TestIsolated(unittest.TestCase):
    def test_no_positional_one_kwonly(self):
        @smart_args
        def check_isolation(*, d: Any = Isolated()):
            d["a"] = 0
            return d

        obj = {"a": 10}
        check_isolation(d=obj)  # if d is not Isolated, it will change
        self.assertEqual(obj["a"], 10)

    def test_no_positional_one_arg(self):
        @smart_args
        def check_isolation(d: Any = Isolated()):
            d["a"] = 0
            return d

        obj = {"a": 10}
        check_isolation(d=obj)  # if d is not Isolated, it will change
        self.assertEqual(obj["a"], 10)

    def test_no_positional_kwonly_and_unused_arg(self):
        @smart_args
        def check_isolation(arg: Any, *, d: Any = Isolated()):
            d["a"] = 0
            return d

        obj = {"a": 10}
        check_isolation(123, d=obj)  # if d is not Isolated, it will change
        self.assertEqual(obj["a"], 10)

    def test_no_positional_one_kwonly_and_one_arg(self):
        @smart_args
        def check_isolation(first: Any = Isolated(), *, second: Any = Isolated()):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(first=obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], 10)

    def test_no_positional_one_kwonly_and_one_not_isolated_arg(self):
        @smart_args
        def check_isolation(first: Any, *, second: Any = Isolated()):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(first=obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], -10)

    def test_no_positional_one_not_isolated_kwonly_and_one_arg(self):
        @smart_args
        def check_isolation(first: Any = Isolated(), *, second: Any):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(first=obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], 0)

    def test_no_positional_one_kwonly_one_isolated_arg_some_not_isolated(self):
        @smart_args
        def check_isolation(par1, par2=3, first: Any = Isolated(), *, second: Any):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(1, first=obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], 0)

    def test_positional_one_kwonly(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(*, d: Any = Isolated()):
            d["a"] = 0
            return d

        obj = {"a": 10}
        check_isolation(d=obj)  # if d is not Isolated, it will change
        self.assertEqual(obj["a"], 10)

    def test_positional_one_arg(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(d: Any = Isolated()):
            d["a"] = 0
            return d

        obj = {"a": 10}
        check_isolation(obj)  # if d is not Isolated, it will change
        self.assertEqual(obj["a"], 10)

    def test_positional_kwonly_and_unused_arg(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(arg: Any, *, d: Any = Isolated()):
            d["a"] = 0
            return d

        obj = {"a": 10}
        check_isolation(123, d=obj)  # if d is not Isolated, it will change
        self.assertEqual(obj["a"], 10)

    def test_positional_one_kwonly_and_one_arg(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(first: Any = Isolated(), *, second: Any = Isolated()):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], 10)

    def test_positional_one_kwonly_and_one_not_isolated_arg(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(first: Any, *, second: Any = Isolated()):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], -10)

    def test_positional_one_not_isolated_kwonly_and_one_arg(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(first: Any = Isolated(), *, second: Any):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], 0)

    def test_positional_one_kwonly_one_isolated_arg_some_not_isolated(self):
        @smart_args(positional_arguments_included=True)
        def check_isolation(par1, par2=3, first: Any = Isolated(), *, second: Any):
            second["a"] = 0
            first["a"] = -10
            return first, second

        obj = {"a": 10}
        first_result, second_result = check_isolation(1, 2, obj, second=obj)  # if d is not Isolated, it will change
        self.assertEqual(first_result["a"], -10)
        self.assertEqual(second_result["a"], 0)
        self.assertEqual(obj["a"], 0)


def get_number_wrapper():
    number = 0

    def inner():
        nonlocal number
        number += 1
        return number

    return inner


class TestEvaluated(unittest.TestCase):
    def test_no_positional_two_args_one_evaluated(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args
        def check_evaluation(x: Any = function_to_evaluate(), y: Any = Evaluated(function_to_evaluate)):
            return x, y

        self.assertEqual(check_evaluation(), (1, 2))

    def test_no_positional_one_evaluated(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args
        def check_evaluation(y: Any = Evaluated(function_to_evaluate)):
            return y

        self.assertEqual(check_evaluation(), 1)

    def test_no_positional_one_evaluated_and_one_kwonly(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args
        def check_evaluation(y: Any = Evaluated(function_to_evaluate), *, additional: Any = None):
            return y

        self.assertEqual(check_evaluation(additional="some"), 1)

    def test_no_positional_one_evaluated_and_one_kwonly_evaluated(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args
        def check_evaluation(x: Any = Evaluated(function_to_evaluate), *, y: Any = Evaluated(function_to_evaluate)):
            return x, y

        self.assertEqual(check_evaluation(), (1, 2))

    def test_no_positional_one_evaluated_and_one_kwonly_evaluated_and_others(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args
        def check_evaluation(
            first,
            x: Any = Evaluated(function_to_evaluate),
            *,
            second,
            y: Any = Evaluated(function_to_evaluate),
            third=None,
        ):
            return x, y

        self.assertEqual(check_evaluation(1, second=2), (1, 2))

    def test_no_positional_no_evaluated(self):
        @smart_args
        def check_evaluation(first, *, second, third=None):
            return first, second

        self.assertEqual(check_evaluation(1, second=2), (1, 2))

    def test_positional_two_args_one_evaluated(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args(positional_arguments_included=True)
        def check_evaluation(x: Any = function_to_evaluate(), y: Any = Evaluated(function_to_evaluate)):
            return x, y

        self.assertEqual(check_evaluation(), (1, 2))

    def test_positional_one_evaluated(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args(positional_arguments_included=True)
        def check_evaluation(y: Any = Evaluated(function_to_evaluate)):
            return y

        self.assertEqual(check_evaluation(), 1)

    def test_positional_one_evaluated_and_one_kwonly(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args(positional_arguments_included=True)
        def check_evaluation(y: Any = Evaluated(function_to_evaluate), *, additional: Any = None):
            return y

        self.assertEqual(check_evaluation(additional="some"), 1)

    def test_positional_one_evaluated_and_one_kwonly_evaluated(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args(positional_arguments_included=True)
        def check_evaluation(x: Any = Evaluated(function_to_evaluate), *, y: Any = Evaluated(function_to_evaluate)):
            return x, y

        self.assertEqual(check_evaluation(), (1, 2))

    def test_positional_one_evaluated_and_one_kwonly_evaluated_and_others(self):
        function_to_evaluate = get_number_wrapper()

        @smart_args(positional_arguments_included=True)
        def check_evaluation(
            first,
            x: Any = Evaluated(function_to_evaluate),
            *,
            second,
            y: Any = Evaluated(function_to_evaluate),
            third=None,
        ):
            return x, y

        self.assertEqual(check_evaluation(1, second=2), (1, 2))

    def test_positional_no_evaluated(self):
        @smart_args(positional_arguments_included=True)
        def check_evaluation(first, *, second, third=None):
            return first, second

        self.assertEqual(check_evaluation(4, second=2), (4, 2))

    def test_positional_non_defined_defaults_after_isolated(self):
        @smart_args(positional_arguments_included=True)
        def support_positionals(x=Isolated(), y=5, /):
            x[0] += 1
            return x, y

        X = [0]
        self.assertEqual(support_positionals(X, 5), ([1], 5))
        self.assertEqual(support_positionals(X), ([1], 5))

    def test_posotional_evaluated_posonly(self):
        @smart_args(positional_arguments_included=True)
        def support_positionals(x, y=Evaluated(lambda: 123), /):
            x[0] += 1
            return x, y

        X = [0]
        self.assertEqual(support_positionals(X), ([1], 123))
