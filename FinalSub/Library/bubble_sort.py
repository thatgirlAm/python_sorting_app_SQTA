# Library/bubble_sort.py

import unittest

def bubble_sort(arr):

    """Sort entered array using bubble sort.

    Examples:
        >>> bubble_sort([12, 42, 1, 4, 73])
        [1, 4, 12, 42, 73]
        >>> bubble_sort(["green", "red", "orange", "blue"])
        ["blue", "green", "orange", "red"]

    Args:
        An input array containing string or number data type.

    Returns:
        An array containing sorted input data.
    """

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr