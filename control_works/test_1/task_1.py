from typing import Callable, Dict, List, Tuple
from datetime import datetime
import inspect
from copy import deepcopy


def print_usage_statistics(func):
    if not isinstance(func, spy):
        raise Exception("function must be decorated")
    for launch in func.launches:
        yield launch


class spy:
    def __init__(self, func: Callable):
        self.func = func
        self.launches: List[Tuple[str, Dict]] = []

    def __call__(self, *args, **kwargs):
        argspec = inspect.getfullargspec(self.func)
        all_arguments = deepcopy(kwargs)
        for arg_name, arg in zip(argspec.args, args):
            all_arguments[arg_name] = arg
        self.launches.append((str(datetime.now()), all_arguments))
        return self.func(*args, **kwargs)
