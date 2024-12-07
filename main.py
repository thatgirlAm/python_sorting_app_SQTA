from tkinter import WORD
import bubble_sort as bs
import quick_sort as qs
import testLib as tst
import unittest
import random
import string
import time
import sorter

# function calling test functions and functions for each sorting algorithms 

testU = unittest.TestLoader().loadTestsFromModule(tst)
unittest.TextTestRunner(verbosity=2).run(testU)

def generate_random_word(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

string_array = [generate_random_word(random.randint(3, 10)) for _ in range(10)]

number_array = [random.randint(0, 1000000) for _ in range(10)]

# string_array1 = ["gfghtr", "sss", "ddc", "qsxc", "etg", "ss", "dsd"]
# number_array1 = [64, 34, 25, 12, 22, 11, 90]

start_time = time.time()
# sorted_list_s = bs.bubble_sort(string_array1)
sorted_list_s = bs.bubble_sort(string_array)
end_time = time.time()
print("Sorted string array using bubble sort: ", sorted_list_s)
print(f"Time taken to sort string array with bubble sort: {end_time - start_time:.2f} seconds")

start_time = time.time()
# sorted_list_n = bs.bubble_sort(number_array1)
sorted_list_n = bs.bubble_sort(number_array)
end_time = time.time()
print("Sorted number array using bubble sort: ", sorted_list_n)
print(f"Time taken to sort number array with bubble sort: {end_time - start_time:.2f} seconds")

start_time = time.time()
# sorted_arr_s = qs.quick_sort(string_array1)
sorted_arr_s = qs.quick_sort(string_array)
end_time = time.time()
print("Sorted string array using quick sort: ", sorted_arr_s)
print(f"Time taken to sort string array with quick sort: {end_time - start_time:.2f} seconds")

start_time = time.time()
# sorted_arr_n = qs.quick_sort(number_array1)
sorted_arr_n = qs.quick_sort(number_array)
end_time = time.time()
print("Sorted number array using quick sort: ", sorted_arr_n)
print(f"Time taken to sort number array with quick sort: {end_time - start_time:.2f} seconds")



start_time = time.time()
# sorted_arr_s = sorter.radix_string(string_array1)
sorted_arr_s = sorter.radix_string(string_array)
end_time = time.time()
print("Sorted string array using radix sort: ", sorted_arr_s)
print(f"Time taken to sort string array with radix sort: {end_time - start_time:.2f} seconds")

start_time = time.time()
# sorted_arr_n = sorter.radix_number(number_array1)
sorted_arr_n = sorter.radix_number(number_array)
end_time = time.time()
print("Sorted number array using radix sort: ", sorted_arr_n)
print(f"Time taken to sort number array with radix sort: {end_time - start_time:.2f} seconds")