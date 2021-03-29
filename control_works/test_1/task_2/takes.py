from typing import Callable, List
from copy import deepcopy
import inspect


def check_types(func: Callable, *types_of_data):
    def inner(*args, **kwargs):
        arguments_list: List = list(deepcopy(args))
        signature = inspect.signature(func)
        for parameter_name, parameter in signature.parameters.items():
            if parameter_name in kwargs:
                arguments_list.append(kwargs[parameter_name])
        for par, type_of_data in zip(arguments_list, types_of_data):
            if not isinstance(par, type_of_data):
                raise TypeError(f"Parameter {par} has wrong type")
        return func(*args, **kwargs)

    return inner


def takes(*types):
    return lambda f: check_types(f, *types)
