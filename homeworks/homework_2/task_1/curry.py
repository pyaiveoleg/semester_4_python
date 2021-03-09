from typing import Callable
import contracts

contracts.CONTRACTS_ENABLED = True


@contracts.pre(lambda func, arity: arity >= 0, "Arity cannot be negative")
def curry_explicit(func: Callable, arity: int) -> Callable:
    """
    Transforms function from several arguments to function that takes arguments sequentially, for example:
    f(a, b, c, d) -> f(a)(b)(c)(d)
    """
    if arity == 0:
        return func
    remaining_curry_level = arity
    args = []

    def curried_function(arg):
        args.append(arg)
        nonlocal remaining_curry_level
        if remaining_curry_level == 1:
            try:
                res = func(*args)
                del args[:]
                remaining_curry_level = arity
                return res
            except Exception:
                raise ValueError("Incorrect arity for this function")
        remaining_curry_level -= 1
        return curried_function

    return curried_function
