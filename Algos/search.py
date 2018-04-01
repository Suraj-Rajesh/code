def binary_search(array, element, begin, end):
    if begin > end:
        return -1

    mid_index = (begin + end)/2

    if element < array[mid_index]:
        return binary_search(array, element, begin, mid_index - 1)
    elif element > array[mid_index]:
        return binary_search(array, element, mid_index + 1, end)
    else:
        return mid_index

if __name__ == '__main__':
    lst = [2, 4, 5, 6, 7, 9]
    print binary_search(lst, 9, 0, len(lst)-1)
