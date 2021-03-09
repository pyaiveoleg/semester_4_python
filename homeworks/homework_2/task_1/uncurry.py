from typing import Callable
import contracts

contracts.CONTRACTS_ENABLED = True


@contracts.pre(lambda func, arity: arity >= 0, "Arity cannot be negative")
def uncurry_explicit(func: Callable, arity: int) -> Callable:
    """
    Transforms function that takes arguments sequentially to function from several arguments, for example:
    f(a)(b)(c)(d) -> f(a, b, c, d)
    """
    if arity == 0:
        return func

    def uncurried_function(*args):
        res = func
        for arg in args:
            res = res(arg)
        return res

    return uncurried_function
