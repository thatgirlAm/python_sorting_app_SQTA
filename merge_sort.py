# STQARASD_Assignment/merge_sort.py

import utilities 

def merge_sort(array):

    """Sort entered array using merge sort.

    Examples:
        >>> merge_sort([12, 42, 1, 4, 73])
        [1, 4, 12, 42, 73]
        >>> merge_sort(["green", "red", "orange", "blue"])
        ["blue", "green", "orange", "red"]

    Args:
        An input array containing string or number data type.

    Returns:
        An array containing sorted input data.
    """

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if compare_strings(left[left_index], right[right_index]):
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    merged_array.extend(left[left_index:])
    merged_array.extend(right[right_index:])

    return merged_array


def compare_strings(str1, str2):
    if not isinstance(str1, str) and not isinstance(str2, str):
        return str1 < str2

    if isinstance(str1, str) and not isinstance(str2, str):
        return False
    if not isinstance(str1, str) and isinstance(str2, str):
        return True

    str1 = str1.lower()
    str2 = str2.lower()

    max_length = max(len(str1), len(str2))
    for i in range(max_length):
        char1 = str1[i] if i < len(str1) else " "
        char2 = str2[i] if i < len(str2) else " "
        rank1 = utilities.LETTERS_RANKING.get(char1, -1)
        rank2 = utilities.LETTERS_RANKING.get(char2, -1)

        if rank1 != rank2:
            return rank1 < rank2

    return len(str1) <= len(str2)

