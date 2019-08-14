# NOTES:
#
# In theory - we assume indexing starts at 1:
#
#   parent = ceil(i/2)
#   left index = i*2
#   right index = i*2 + 1
#
#   In practice - indexing starts at 0, so we need to tweak:
#
#   parent = (i - 1)/2
#   left index = i*2 + 1
#   right index = i*2 + 2
#

# O(logn)
def maxheapify(arr, index):
    n = len(arr)

    left_index = 2*index + 1
    right_index = 2*index + 2

    # assume element at index(node) is greatest
    greatest_index = index

    # now compare node, left and right, see if they form a heap
    # if not, adjust and do heapify on changed child node
    if left_index < n and arr[left_index] > arr[index]:
        # swap first
        arr[left_index], arr[greatest_index] = arr[greatest_index], arr[left_index]
        # now set greatest_index to appropriate index value
        greatest_index = left_index

    # note here, we are comparing with greatest_index, since we already
    # compared and set greatest_index to one among left or node
    if right_index < n and arr[right_index] > arr[greatest_index]:
        # swap first
        arr[right_index], arr[greatest_index] = arr[greatest_index], arr[right_index]
        # now set greatest_index to appropriate index value
        greatest_index = right_index

    # if re-arranged, then we need to heapify on the index we swapped
    if greatest_index != index:
        maxheapify(arr, greatest_index)

# given an array, covert into a heap (maxheap in this case)
# O(n)
def create_heap(arr):
    n = len(arr)
    # if we look at heapify algorithm, we can observe, all leaf nodes are heaps
    # by themselves, so no need to bother heapifying them. So, we can ignore those.
    # For a tree of n elements, number of non-leaf nodes are n/2, thus applying
    # to only 0 -> (n/2 - 1) index elements
    for i in reversed(range(n/2)):
        maxheapify(arr, i)

def heap_filter_up(arr, index):
    par_index = (index - 1)/2
    if par_index >= 0:
        if arr[par_index] < arr[index]:
            arr[par_index], arr[index] = arr[index], arr[par_index]
            heap_filter_up(arr, par_index)

# O(logn)
def insert(arr, data):
    arr.append(data)
    n = len(arr)
    index = n - 1
    heap_filter_up(arr, index)


# we assume arr is already heapified
# O(logn)
def delete(arr):
    if len(arr) == 1:
        return arr.pop()

    ret_elem = arr[0]
    arr[0] = arr.pop()
    maxheapify(arr, 0)
    return ret_elem

# O(nlogn)
def heapsort(arr):
    create_heap(arr)

    sorted_array = []
    for _ in range(len(arr)):
        sorted_array.append(delete(arr))

    return sorted_array


# CREATE HEAP - O(n)
in_array = [3, 4, 1, 2, 5]
create_heap(in_array)
print in_array

# INSERT - O(logn)
# if we do n inserts, then, O(nlogn)
in_array = []
insert(in_array, 1)
insert(in_array, 3)
insert(in_array, 2)
insert(in_array, 4)
insert(in_array, 5)
insert(in_array, 0)
insert(in_array, 4)
print in_array

# DELETE - O(logn)
in_array = [3, 4, 1, 2, 5]
create_heap(in_array)
print delete(in_array)

# HEAPSORT - O(nlogn)
in_array = [3, 4, 1, 2, 5]
print heapsort(in_array)
