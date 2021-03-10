from typing import Callable
import contracts

contracts.CONTRACTS_ENABLED = True


@contracts.pre(lambda func, arity: arity >= 0, "Arity cannot be negative")
def curry_explicit(func: Callable, arity: int) -> Callable:
    """
    Transforms function from several arguments to function that takes arguments sequentially, for example:
    f(a, b, c, d) -> f(a)(b)(c)(d)
    """

    def inner_fun(*args) -> Callable:
        if len(args) == arity:
            return func(*args)
        if len(args) > arity:
            raise ValueError("Quantity of args should be equal to arity")
        return lambda arg: inner_fun(*args, arg)  # we add one argument with each function call

    return inner_fun
