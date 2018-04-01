from functools import partial
from timeit import timeit


def fibonacci_cached(n):
    if n not in cache:
        cache[n] = fibonacci_cached(n-1) + fibonacci_cached(n-2)

    return cache[n]


def fibonacci_uncached(n):
    if n == 1 or n == 2:
        return 1
    else:
        ret = fibonacci_uncached(n-1) + fibonacci_uncached(n-2)
        return ret


cache = {1:1, 2:1}
print fibonacci_cached(8)
print cache
print timeit(partial(fibonacci_cached, 80), number=1)
print timeit(partial(fibonacci_uncached, 80), number=1)
