from tkinter import WORD
import bubble_sort as bs
import quick_sort as qs
import merge_sort as ms
import sorter as rs
import testLib as tst
import unittest
import time
import utilities


# function calling test functions and functions for each sorting algorithms 
testU = unittest.TestLoader().loadTestsFromModule(tst)
unittest.TextTestRunner(verbosity=2).run(testU)

performanceData = []
dataSize = 10
index2Check = 7
string_array = utilities.generate_StringArray(dataSize)
number_array = utilities.generate_numberArray(dataSize)
numbDict = {}
strDict = {}
utilities.createRecord(strDict, string_array)
utilities.createRecord(numbDict, number_array)
strVal = list(strDict.values())
numbVal = list(numbDict.values())

print("Unsorted String Array: ", string_array)
print("Unsorted Number Array: ", number_array)

start_time = time.time()
sorted_arr_s = bs.bubble_sort(string_array)
end_time = time.time()
print("Sorted string array using bubble sort: ", sorted_arr_s)
utilities.add_data(performanceData, 1, "Bubble Sort with String data", end_time-start_time)
index_str = strVal.index(sorted_arr_s[index2Check])
print("Sorted arrays' element: ", sorted_arr_s[index2Check], " at index: ", index2Check, " is at index: ", index_str, " in the original array")

start_time = time.time()
sorted_arr_n = bs.bubble_sort(number_array)
end_time = time.time()
print("Sorted number array using bubble sort: ", sorted_arr_n)
utilities.add_data(performanceData, 2, "Bubble Sort with number data", end_time-start_time)
index_numb = numbVal.index(sorted_arr_n[index2Check])
print("Sorted arrays' element: ", sorted_arr_n[index2Check], " at index: ", index2Check, " is at index: ", index_numb, " in the original array")

start_time = time.time()
sorted_arr_s = qs.quick_sort(string_array)
end_time = time.time()
print("Sorted string array using quick sort: ", sorted_arr_s)
utilities.add_data(performanceData, 3, "Quick Sort with String data", end_time-start_time)
index_str = strVal.index(sorted_arr_s[index2Check])
print("Sorted arrays' element: ", sorted_arr_s[index2Check], " at index: ", index2Check, " is at index: ", index_str, " in the original array")

start_time = time.time()
sorted_arr_n = qs.quick_sort(number_array)
end_time = time.time()
print("Sorted number array using quick sort: ", sorted_arr_n)
utilities.add_data(performanceData, 4, "Quick Sort with number data", end_time-start_time)
index_numb = numbVal.index(sorted_arr_n[index2Check])
print("Sorted arrays' element: ", sorted_arr_n[index2Check], " at index: ", index2Check, " is at index: ", index_numb, " in the original array")

start_time = time.time()
sorted_arr_s = rs.radix_sort(string_array)
end_time = time.time()
print("Sorted string array using radix sort: ", sorted_arr_s)
utilities.add_data(performanceData, 5, "Radix Sort with String data", end_time-start_time)
index_str = strVal.index(sorted_arr_s[index2Check])
print("Sorted arrays' element: ", sorted_arr_s[index2Check], " at index: ", index2Check, " is at index: ", index_str, " in the original array")

start_time = time.time()
sorted_arr_n = rs.radix_sort(number_array)
end_time = time.time()
print("Sorted number array using radix sort: ", sorted_arr_n)
utilities.add_data(performanceData, 6, "Radix Sort with number data", end_time-start_time)
index_numb = numbVal.index(sorted_arr_n[index2Check])
print("Sorted arrays' element: ", sorted_arr_n[index2Check], " at index: ", index2Check, " is at index: ", index_numb, " in the original array")

start_time = time.time()
sorted_arr_s = ms.merge_sort(string_array)
end_time = time.time()
print("Sorted string array using merge sort: ", sorted_arr_s)
utilities.add_data(performanceData, 7, "Merge Sort with String data", end_time-start_time)
index_str = strVal.index(sorted_arr_s[index2Check])
print("Sorted arrays' element: ", sorted_arr_s[index2Check], " at index: ", index2Check, " is at index: ", index_str, " in the original array")

start_time = time.time()
sorted_arr_n = ms.merge_sort(number_array)
end_time = time.time()
print("Sorted number array using merge sort: ", sorted_arr_n)
utilities.add_data(performanceData, 8, "Merge Sort with number data", end_time-start_time)
index_numb = numbVal.index(sorted_arr_n[index2Check])
print("Sorted arrays' element: ", sorted_arr_n[index2Check], " at index: ", index2Check, " is at index: ", index_numb, " in the original array")

utilities.export2CSV(performanceData)