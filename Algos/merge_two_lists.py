a = [4, 5, 7]
b = [1, 2, 3]

def merge(a, b):
    res = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    if i == len(a):
        res += b[j:]
    elif j == len(b):
        res += a[i:]

    return res

print merge(a, b)
