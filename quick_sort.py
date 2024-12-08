# STQARASD_Assignment/quick_sort.py

import unittest

def quick_sort(arr):

    """Sort entered array using quick sort.

    Examples:
        >>> quick_sort([12, 42, 1, 4, 73])
        [1, 4, 12, 42, 73]
        >>> quick_sort(["green", "red", "orange", "blue"])
        ["blue", "green", "orange", "red"]

    Args:
        An input array containing string or number data type.

    Returns:
        An array containing sorted input data.
    """

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)