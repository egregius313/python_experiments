from functools import wraps
import turtle

from toolz import memoize


def tortuga(f):
    @wraps(f)
    def turtled(n):
        if isinstance(n, int):
            turtle.color('red' if n % 2 else 'green')
        turtle.left(10)
        turtle.forward(n)
        return f(n)
    return turtled


@tortuga
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@tortuga
@memoize
def mem_fib(n):
    if n < 2:
        return n
    return mem_fib(n - 1) + mem_fib(n - 2)
    
        
    
