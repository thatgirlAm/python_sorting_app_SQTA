import utilities 

def merge_sort(array):
    # Base case: if the array has one or no elements, it's already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursive calls to sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged_array = []
    left_index = 0
    right_index = 0

    # Merge until one of the arrays is exhausted
    while left_index < len(left) and right_index < len(right):
        if compare_strings(left[left_index], right[right_index]):
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    # Append the remaining elements
    merged_array.extend(left[left_index:])
    merged_array.extend(right[right_index:])

    return merged_array


def compare_strings(str1, str2):
    # Transform strings to lowercase for case-insensitive comparison
    str1 = str1.lower()
    str2 = str2.lower()

    # Compare character by character using LETTERS_RANKING
    max_length = max(len(str1), len(str2))
    for i in range(max_length):
        char1 = str1[i] if i < len(str1) else " "
        char2 = str2[i] if i < len(str2) else " "
        rank1 = utilities.LETTERS_RANKING.get(char1, -1)
        rank2 = utilities.LETTERS_RANKING.get(char2, -1)

        if rank1 != rank2:
            return rank1 < rank2  # Return True if char1 comes before char2

    return len(str1) <= len(str2)  # Tie-breaker: shorter strings come first


print(merge_sort(["Banana", "apple", "Orange", "banana", "APPLE"]))
print(merge_sort([38, 27, "apple", 3, "banana"]))