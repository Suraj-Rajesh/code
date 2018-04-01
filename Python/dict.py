colors = ['red', 'yellow', 'green', 'yellow', 'blue']

# get default values to a dictionary, without checking(for a KeyError) if the
# key is present

d = dict()
for color in colors:
    d[color] = d.get(color, 0) + 1

print d

# same using defaultdict

from collections import defaultdict
dd = defaultdict(int)

for color in colors:
    dd[color] = dd[color] + 1

print dict(dd)
