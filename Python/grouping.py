from collections import defaultdict

name_list = ['mounika', 'koshy', 'ashok', 'gurleen']

d = defaultdict(list)

for name in name_list:
    l = len(name)
    d[l].append(name)
print d
