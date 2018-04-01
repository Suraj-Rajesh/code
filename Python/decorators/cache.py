from functools import wraps


def cache(func):
    memo = {}
    @wraps(func)
    def wrapper(x):
        print 'memo: ' + str(memo)
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return wrapper

@cache
def fn(x):
    return x + 1

fn(1)
fn(1)
fn(3)
