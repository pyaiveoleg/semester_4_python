import inspect
from copy import deepcopy
from typing import Callable


def smart_args(function: Callable = None, *, positional_arguments_included: bool = False):
    """
    Adds ability to evaluate value before every launch or make copy of it.
    Usage:
    To add evaluation, use Evaluated(function) as default arg of your function
    To add deep copy of mutable argument, use Isolated() as default arg of your function.

    You can add support of positional arguments using positional_arguments_included=True
    """
    if function is None:
        return lambda f: smart_args(f, positional_arguments_included=positional_arguments_included)

    def inner(*args, **kwargs):
        argspec = inspect.getfullargspec(function)
        args_list = list(args)

        if argspec.defaults is not None:
            defaults_quantity = len(argspec.defaults)
            for index, (name, default) in enumerate(zip(argspec.args[-defaults_quantity:], argspec.defaults)):
                name_in_args = len(args) > len(argspec.args) - defaults_quantity + index
                if isinstance(default, Isolated):  # isolated need to be set: in kwargs or in args
                    if name in kwargs:
                        kwargs[name] = deepcopy(kwargs[name])
                    elif positional_arguments_included:
                        index_to_isolate = len(argspec.args) - defaults_quantity + index
                        args_list[index_to_isolate] = deepcopy(args_list[index_to_isolate])
                elif isinstance(default, Evaluated):
                    if name not in kwargs and (
                        not name_in_args and positional_arguments_included or not positional_arguments_included
                    ):
                        args_list.append(default())
                    elif not name_in_args:
                        args_list.append(default)
                elif not name_in_args:
                    args_list.append(default)

        if argspec.kwonlydefaults is not None:
            for name in argspec.kwonlyargs[-len(argspec.kwonlydefaults) :]:
                default = argspec.kwonlydefaults[name]
                if isinstance(default, Isolated):
                    kwargs[name] = deepcopy(kwargs[name])
                if isinstance(default, Evaluated):
                    if name not in kwargs:
                        kwargs[name] = default()
        return function(*args_list, **kwargs)

    return inner


class Isolated:
    def __init__(self):
        pass


class Evaluated:
    def __init__(self, function: Callable):
        self._function = function

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)
