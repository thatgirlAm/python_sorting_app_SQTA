def radix_sort(array):
    
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

    # Count occurrences of digits
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Update count array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy to the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort_numbers(arr):
    """
    Performs Radix Sort on an array of numbers.
    """
    if not arr:
        return []

    # Find the maximum number
    max_num = max(arr)

    # Sort based on each digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_numbers(arr, exp)
        exp *= 10

    return arr


def counting_sort_for_strings(arr, pos):
    """
    A helper function for Radix Sort that performs counting sort based on string characters.
    """
    n = len(arr)
    output = [""] * n
    count = [0] * 256  # For all ASCII characters

    # Count occurrences of characters at position `pos`
    for string in arr:
        char = string[pos] if pos < len(string) else chr(0)  # Pad shorter strings
        count[ord(char)] += 1

    # Update count array
    for i in range(1, 256):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        char = arr[i][pos] if pos < len(arr[i]) else chr(0)
        output[count[ord(char)] - 1] = arr[i]
        count[ord(char)] -= 1

    # Copy to the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort_strings(arr):
    """
    Performs Radix Sort on an array of strings.
    """
    if not arr:
        return []

    # Find the length of the longest string
    max_length = max(len(s) for s in arr)

    # Sort based on each character from right to left
    for pos in range(max_length - 1, -1, -1):
        counting_sort_for_strings(arr, pos)

    return arr
