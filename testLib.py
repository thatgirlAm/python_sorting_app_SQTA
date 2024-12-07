import unittest
import bubble_sort as bs
import quick_sort as qs

class Test_testLib(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(bs.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(qs.quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(bs.bubble_sort(["apple", "banana", "cherry", "date", "elderberry", "fig"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])
        self.assertEqual(qs.quick_sort(["apple", "banana", "cherry", "date", "elderberry", "fig"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])

    def test_unsorted_array(self):
        self.assertEqual(bs.bubble_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(qs.quick_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(bs.bubble_sort(["sjsi", "asa", "dieszc", "osrwn", "eyba", "yernhsb", "tebsxj"]), ['asa', 'dieszc', 'eyba', 'osrwn', 'sjsi', 'tebsxj', 'yernhsb'])
        self.assertEqual(qs.quick_sort(["sjsi", "asa", "dieszc", "osrwn", "eyba", "yernhsb", "tebsxj"]), ['asa', 'dieszc', 'eyba', 'osrwn', 'sjsi', 'tebsxj', 'yernhsb'])

    def test_single_element_array(self):
        self.assertEqual(bs.bubble_sort([42]), [42])
        self.assertEqual(qs.quick_sort([42]), [42])
        self.assertEqual(bs.bubble_sort(["eliu"]), ["eliu"])
        self.assertEqual(qs.quick_sort(["eliu"]), ["eliu"])

    def test_empty_array(self):
        self.assertEqual(bs.bubble_sort([]), [])
        self.assertEqual(qs.quick_sort([]), [])

    def test_reverse_sorted_array(self):
        self.assertEqual(bs.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(qs.quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(bs.bubble_sort(["fig", "elderberry", "date", "cherry", "banana", "apple"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])
        self.assertEqual(qs.quick_sort(["fig", "elderberry", "date", "cherry", "banana", "apple"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])

    def test_duplicate_elements(self):
        self.assertEqual(bs.bubble_sort([4, 2, 2, 8, 5, 5, 5, 1]), [1, 2, 2, 4, 5, 5, 5, 8])
        self.assertEqual(qs.quick_sort([4, 2, 2, 8, 5, 5, 5, 1]), [1, 2, 2, 4, 5, 5, 5, 8])
        self.assertEqual(bs.bubble_sort(["apple", "banana", "cherry", "apple", "banana", "date", "cherry", "fig"]), ['apple', 'apple', 'banana', 'banana', 'cherry', 'cherry', 'date', 'fig'])
        self.assertEqual(qs.quick_sort(["apple", "banana", "cherry", "apple", "banana", "date", "cherry", "fig"]), ['apple', 'apple', 'banana', 'banana', 'cherry', 'cherry', 'date', 'fig'])

    def test_negative_numbers(self):
        self.assertEqual(bs.bubble_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])
        self.assertEqual(qs.quick_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])

    def test_sensitivity_string(self):
        self.assertEqual(bs.bubble_sort(["Apple", "apple", "Banana", "banana"]), ["Apple", "Banana", "apple", "banana"])
        self.assertEqual(qs.quick_sort(["Apple", "apple", "Banana", "banana"]), ["Apple", "Banana", "apple", "banana"])



    # def validate_array(user_input):
    #     for item in user_input:
    #         if not item.isalnum():  # Check if the item is not alphanumeric
    #             raise ValueError(f"Invalid element '{item}' detected! Only alphabets and digits are allowed.")
    #     return user_input

    # try:
    #     # Get input from the user
    #     user_input = input("Enter elements separated by spaces (only alphabets or digits): ").split()

    #     # Validate the input
    #     valid_array = validate_array(user_input)
    #     print("Valid array:", valid_array)

    # except ValueError as e:
    #     print("Error:", e)









if __name__ == '__main__':
    unittest.main()
