def partition(arr, low, high):
    pivot = arr[low]
    border = low

    for i in range(low, high + 1):
        if arr[i] < pivot:
            border += 1
            arr[border], arr[i] = arr[i], arr[border]

    arr[low], arr[border] = arr[border], arr[low]
    return border

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


arr = [4,5,1,2,6,7]
quicksort(arr, 0, len(arr) - 1)
print arr
