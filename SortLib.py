from sortLibCU.bubble_sort import bubble_sort
from sortLibCU.quick_sort import quick_sort
from sortLibCU.bubble_sort import bubble_sort
from sortLibCU.quick_sort import quick_sort
from sortLibCU.tests import sortLibCU
import unittest

testU = unittest.TestLoader().loadTestsFromModule(sortLibCU)
unittest.TextTestRunner(verbosity=2).run(testU)

unsorted_list_s = ["gfghtr", "sss", "ddc", "qsxc", "etg", "ss", "dsd"]
unsorted_list_n = [64, 34, 25, 12, 22, 11, 90]
sorted_list_s = bubble_sort(unsorted_list_s)
sorted_list_n = bubble_sort(unsorted_list_n)
print("Sorted list string:", sorted_list_s)
print("Sorted list number:", sorted_list_n)

arr_s = ["xxssa", "pewjn", "ergoir", "lnasa", "aagv", "ujsd", "hrth"]
arr_n = [3, 6, 8, 10, 1, 2, 1]
sorted_arr_s = quick_sort(arr_s)
sorted_arr_n = quick_sort(arr_n)
print("Sorted array string:", sorted_arr_s)
print("Sorted array number:", sorted_arr_n)
