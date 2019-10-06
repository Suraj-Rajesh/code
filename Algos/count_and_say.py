def next_term(term):
    res = ''

    count = 1
    prev = term[0]
    n = len(term)
    for i in range(1, n):
        if term[i] == prev:
            count += 1
        else:
            res += '{}{}'.format(str(count), prev)
            count = 1

        prev = term[i]

    res += '{}{}'.format(str(count), prev)
    return res


def count_say(n):
    if n == 1:
        return '1'

    res = '11'
    for i in range(2, n):
        res = next_term(res)

    return res

print(count_say(5))
