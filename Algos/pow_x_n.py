def pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1/x

    res = pow(x, n/2)
    if n%2 == 0:
        return res * res
    else:
        return  res* res * x

print pow(0.44528, 0)
