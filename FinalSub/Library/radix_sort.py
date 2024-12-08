# Library/radix_sort.py

def radix_sort(array):
    
    """Sort entered array using radix sort.

    Examples:
        >>> radix_sort([12, 42, 1, 4, 73])
        [1, 4, 12, 42, 73]
        >>> radix_sort(["green", "red", "orange", "blue"])
        ["blue", "green", "orange", "red"]

    Args:
        An input array containing string or number data type.

    Returns:
        An array containing sorted input data.
    """

    for x in array:
        if isinstance(x, int):
            numbers = [x for x in array if isinstance(x, int)]
            return radix_sort_numbers(numbers)
        elif isinstance(x, str):
            strings = [x for x in array if isinstance(x, str)]
            return radix_sort_strings(strings)
        else:
            pass

def counting_sort_for_numbers(arr, exp):
    """
    A helper function for Radix Sort that performs counting sort based on digits.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort_numbers(arr):

    if not arr:
        return []

    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort_for_numbers(arr, exp)
        exp *= 10

    return arr


def counting_sort_for_strings(arr, pos):

    n = len(arr)
    output = [""] * n
    count = [0] * 256

    for string in arr:
        char = string[pos] if pos < len(string) else chr(0)
        count[ord(char)] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        char = arr[i][pos] if pos < len(arr[i]) else chr(0)
        output[count[ord(char)] - 1] = arr[i]
        count[ord(char)] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort_strings(arr):

    if not arr:
        return []

    max_length = max(len(s) for s in arr)

    for pos in range(max_length - 1, -1, -1):
        counting_sort_for_strings(arr, pos)

    return arr
