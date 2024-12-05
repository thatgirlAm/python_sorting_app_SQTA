import unittest
from sortLibCU.bubble_sort import bubble_sort
from sortLibCU.quick_sort import quick_sort

class Test_sortLibCU(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort(["apple", "banana", "cherry", "date", "elderberry", "fig"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])
        self.assertEqual(quick_sort(["apple", "banana", "cherry", "date", "elderberry", "fig"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])

    def test_unsorted_array(self):
        self.assertEqual(bubble_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quick_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(bubble_sort(["sjsi", "asa", "dieszc", "osrwn", "eyba", "yernhsb", "tebsxj"]), ['asa', 'dieszc', 'eyba', 'osrwn', 'sjsi', 'tebsxj', 'yernhsb'])
        self.assertEqual(quick_sort(["sjsi", "asa", "dieszc", "osrwn", "eyba", "yernhsb", "tebsxj"]), ['asa', 'dieszc', 'eyba', 'osrwn', 'sjsi', 'tebsxj', 'yernhsb'])

    def test_single_element_array(self):
        self.assertEqual(bubble_sort([42]), [42])
        self.assertEqual(quick_sort([42]), [42])
        self.assertEqual(bubble_sort(["eliu"]), ["eliu"])
        self.assertEqual(quick_sort(["eliu"]), ["eliu"])

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(quick_sort([]), [])

    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort(["fig", "elderberry", "date", "cherry", "banana", "apple"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])
        self.assertEqual(quick_sort(["fig", "elderberry", "date", "cherry", "banana", "apple"]), ["apple", "banana", "cherry", "date", "elderberry", "fig"])

    def test_duplicate_elements(self):
        self.assertEqual(bubble_sort([4, 2, 2, 8, 5, 5, 5, 1]), [1, 2, 2, 4, 5, 5, 5, 8])
        self.assertEqual(quick_sort([4, 2, 2, 8, 5, 5, 5, 1]), [1, 2, 2, 4, 5, 5, 5, 8])
        self.assertEqual(bubble_sort(["apple", "banana", "cherry", "apple", "banana", "date", "cherry", "fig"]), ['apple', 'apple', 'banana', 'banana', 'cherry', 'cherry', 'date', 'fig'])
        self.assertEqual(quick_sort(["apple", "banana", "cherry", "apple", "banana", "date", "cherry", "fig"]), ['apple', 'apple', 'banana', 'banana', 'cherry', 'cherry', 'date', 'fig'])

    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])
        self.assertEqual(quick_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])

    def test_sensitivity_string(self):
        self.assertEqual(bubble_sort(["Apple", "apple", "Banana", "banana"]), ["Apple", "Banana", "apple", "banana"])
        self.assertEqual(quick_sort(["Apple", "apple", "Banana", "banana"]), ["Apple", "Banana", "apple", "banana"])

if __name__ == '__main__':
    unittest.main()
