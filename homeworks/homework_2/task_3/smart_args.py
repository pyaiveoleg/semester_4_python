import inspect
from copy import deepcopy
from typing import Callable


def smart_args(function: Callable = None, positional_arguments_included: bool = False):
    """
    Adds ability to evaluate value before every launch or make copy of it.
    Usage:
    To add evaluation, use Evaluated(function) as default arg of your function
    To add deep copy of mutable argument, use Isolated() as default arg of your function.

    You can add support of positional arguments using positional_arguments_included=True
    """
    if function is None:
        return lambda f: smart_args(f, positional_arguments_included)

    def inner(*args, **kwargs):
        a = inspect.getfullargspec(function)
        # print(a)

        if a.defaults is not None:
            defaults_quantity = len(a.defaults)
            for index, (name, default) in enumerate(zip(a.args[-defaults_quantity:], a.defaults)):
                if isinstance(default, Isolated):  # isolated need to be set: in kwargs or in args
                    if name in kwargs:
                        kwargs[name] = deepcopy(kwargs[name])
                    elif positional_arguments_included:
                        args_list = list(args)
                        args_list[-defaults_quantity + index] = deepcopy(args_list[-defaults_quantity + index])
                        args = tuple(args_list)
                if isinstance(default, Evaluated):
                    name_in_args = len(args) > len(a.args) - defaults_quantity + index
                    if name not in kwargs:
                        if not name_in_args and positional_arguments_included or not positional_arguments_included:
                            kwargs[name] = default()

        if a.kwonlydefaults is not None:
            for name in a.kwonlyargs[-len(a.kwonlydefaults):]:
                default = a.kwonlydefaults[name]
                if isinstance(default, Isolated):
                    kwargs[name] = deepcopy(kwargs[name])
                if isinstance(default, Evaluated):
                    if name not in kwargs:
                        kwargs[name] = default()

        return function(*args, **kwargs)
    return inner


class Isolated:
    def __init__(self):
        pass


class Evaluated:
    def __init__(self, function: Callable):
        self._function = function

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)
