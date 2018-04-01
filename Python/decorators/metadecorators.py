from functools import wraps

def include_original(decorator):
    def decorator_wrapper(func):
        decorated = decorator(func)
        decorated._original = func
        return decorated
    return decorator_wrapper

@include_original
def fn_handler(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        print 'Before call: ' + func.__name__
        return func(*args, **kwargs)
        print 'After call: ' + func.__name__
    return func_wrapper

@fn_handler
def hello():
    return 'Hellow !!'

#print hello()
print hello._original()
