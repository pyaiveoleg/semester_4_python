from typing import Callable
import contracts

from homeworks.homework_2.task_2.function_with_cache import FunctionWithCache

contracts.CONTRACTS_ENABLED = True


@contracts.pre(lambda func=None, *, size: size >= 0, "Size cannot be negative")
def enable_cache(func: Callable = None, *, size: int = 0):
    """
    Decorator that adds cache to any function: if function had already launched with some parameters, next
    call with these parameters will show you the old result

    :param func: function (you don't need to use this parameter in decorator)
    :param size: max quantity of records in cache: old ones are deleted if cache overflows
    :return: function with cache
    """

    if func is None:
        return lambda f: enable_cache(f, size=size)  # to pass here function that is defined after decorator

    return FunctionWithCache(func, size)
