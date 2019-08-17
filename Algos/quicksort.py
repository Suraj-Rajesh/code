# METHOD 1 - Preferred method (using two pointers for partitioning)

def quickSort(arr, low, high):
  if low < high:
      p = partition(arr, low, high)
      quickSort(arr, low, p - 1)
      quickSort(arr, p + 1, high)

def partition(arr, low, high):
  pivot = arr[low]
  left = low + 1
  right = high

  while left <= right:
      while left <= right and arr[left] <= pivot:
          left += 1

      while left <= right and arr[right] > pivot:
          right -= 1

      if left < right:
          # swap
          arr[left], arr[right] = arr[right], arr[left]

  # swap
  arr[low], arr[right] = arr[right], arr[low]
  return right

arr = [10, 9, 8]
quickSort(arr, 0, len(arr) - 1)
print(arr)

arr = [54,17,26,93,17,77,31,44,55,20]
quickSort(arr, 0, len(arr) - 1)
print(arr)

arr = [10, 12, 15, 3, 20]
quickSort(arr, 0, len(arr) - 1)
print(arr)

# METHOD 2 - using one pointer (number of swaps are more and less efficient)

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
