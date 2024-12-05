# Unit tests
import unittest

# QuickSort function
def quick_sort(arr):
    if len(arr) <= 1:  # Base case: an array of 0 or 1 elements is already sorted
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine