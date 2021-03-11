from typing import Callable, OrderedDict as OrderedDictType
from collections import OrderedDict
from functools import update_wrapper


class FunctionWithCache:
    def __init__(self, function: Callable, size: int):
        self._function = function
        self.size = size
        self.cache: OrderedDictType = OrderedDict()
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        if self.size == 0:
            return self._function(*args, **kwargs)
        key = args + tuple(sorted(kwargs.items()))
        if key in self.cache:
            print("result from cache: ", end="")
            return self.cache[key]

        result = self._function(*args, **kwargs)
        if len(self.cache) >= self.size:
            self.cache.popitem(last=False)  # deletes first element
        self.cache[key] = result
        return result
