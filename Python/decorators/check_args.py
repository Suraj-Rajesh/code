def check_for_negative(func):
    def helper(x):
        if x > 0: return func(x)
        else: raise Exception('Negative values not allowed')

    return helper

@check_for_negative
def adder(x):
    return x + 1

try:
    print adder(-2)
except Exception as details:
    print details
