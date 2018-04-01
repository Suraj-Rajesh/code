from sort_algos import bubble_sort

def test_bubble_sort():
    assert([1, 2, 3, 4, 5] == bubble_sort([4, 3, 5, 1, 2]))

def test_bubble_sort_sorted():
    assert([1, 2, 3, 4, 5] == bubble_sort([1, 2, 3, 4, 5]))
