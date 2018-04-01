# 
# Using timeit 
#

# A problem with timeit is that, we need to define all local vars inside the
# timeit call.
# 
# For example:
#   timeit('lst = range(100); lst.pop(0)', number=5)
# 
# But, here we only want to time the pop of the first time for list vs deque
# We do not want to time the creation of the list and deque(FYI, creation of
# list is faster than a deque). In such scenarios, use timeit as shown below
# to include already defined functions and variables.

# create a list
lst = range(100000)

# create a deque of same size as that of the list
from collections import deque
dq = deque(range(100000))

# pops first item of deque
def deque_pop(d):
    d.popleft()

# pops first item of the list
def list_pop(l):
    l.pop(0)

from timeit import timeit, Timer

# time list popping(first item of the list) 99999 times
t = Timer('list_pop(lst)', setup='from __main__ import list_pop, lst')
print t.timeit(99999)

# time deque pop(leftmost item) 99999 times
t = Timer('deque_pop(dq)', setup='from __main__ import deque_pop, dq')
print t.timeit(99999)
