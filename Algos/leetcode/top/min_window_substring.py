import collections


#s = 'ADOBECODEBANC'
s = 'ADOBANCECODEBNC'
t = 'ABC'

def minwindow(s, t):
    begin = end = 0
    n = len(s)
    res = (0, n + 1)

    needed_map = collections.Counter(t)
    needed_count = len(needed_map)

    while end < n:
        while end < n and needed_count > 0:
            if s[end] in needed_map:
                needed_map[s[end]] -= 1
                if needed_map[s[end]] == 0:
                    needed_count -= 1
            end += 1

        while begin < end and needed_count == 0:
            if s[begin] in needed_map:
                needed_map[s[begin]] += 1
                if needed_map[s[begin]] > 0:
                    needed_count += 1
            begin += 1

        # res contains indices that should include the sub-string
        res = (begin - 1, end - 1) if end - begin < res[1] - res[0] else res

    if res[1] - res[0] < n + 1:
        print(res)
        return s[res[0]:res[1] + 1]
    else:
        return ''

print(minwindow(s, t))
