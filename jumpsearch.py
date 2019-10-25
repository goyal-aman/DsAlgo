"""
refrence from geeksforgeeks
"""
from math import sqrt


def JumpSearch(arr, item_to_search):
    """
    for sorted arrays
    """
    arr_len = len(arr)
    prev = 0
    step = jump = int(sqrt(arr_len))

    while arr[min(step, n) - 1] < item_to_search:
        prev = step
        step += jump
        if prev >= n:
            return -1
    while prev < min(step, n):
        prev += 1
        if arr[prev - 1] == item_to_search:
            return prev - 1
    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 610
n = len(arr)

# Find the index of 'x' using Jump Search
for i in arr:
    index = JumpSearch(arr, i)
    print(f"item {i}: {index}")
