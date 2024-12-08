from tkinter import WORD
import bubble_sort as bs
import quick_sort as qs
import merge_sort as ms
import radix_sort as rs
import testLib as tst
import unittest
import time
import utilities
import re


# function calling test functions and functions for each sorting algorithms 
testU = unittest.TestLoader().loadTestsFromModule(tst)
unittest.TextTestRunner(verbosity=2).run(testU)

performanceData = []
ncr = []
scr = []
numbDict = {}
strDict = {}

def enterData():
    user_data_input = input("Enter elements separated by spaces (mix of numbers and strings): ").split()
    number_array = []
    string_array = []
    for item in user_data_input:
        
        print(item)
        print(type(item))

        # if(check_user_number(item)):
        if(item.isdigit()):
            number_array.append(item)
        elif not (bool(re.search(r'[^A-Za-z0-9]', item))):
            string_array.append(item)
        else:
            pass

    print("number: ", number_array, " str: ", string_array)
    return number_array, string_array

def generateStringData():
    dataSize = int(input("Enter the size of string array to be generated: "))
    string_array = utilities.generate_StringArray(dataSize)
    print("Original string array: ",string_array)
    return string_array

def generateNumberData():
    dataSize = int(input("Enter the size of number array to be generated: "))
    number_array = utilities.generate_numberArray(dataSize)
    print("Original number array: ",number_array)
    return number_array

user_input = int(input("Enter 1 to enter input array or Enter 2 to auto-generate string input arrays or Enter 3 to auto-generate number input arrays: "))

if user_input == 1:
    number_array, string_array = enterData()
    scr = string_array
    ncr = number_array
elif user_input == 2:
    string_array = generateStringData()
    scr = string_array
elif user_input == 3:
    number_array = generateNumberData()
    ncr = number_array
else:
    print("Invalid Option!")
    pass


utilities.createRecord(strDict, scr)
utilities.createRecord(numbDict, ncr)
strVal = list(strDict.values())
numbVal = list(numbDict.values())

index2Check = int(input("Enter index value of element in sorted array to check its index in original array: "))

algorithms = {
        ms.merge_sort,
        rs.radix_sort,
        qs.quick_sort,
        bs.bubble_sort
    }
i = 0
for algo in algorithms:
    print("1 number: ", number_array, " str: ", string_array)
    if len(string_array) != 0:
        start_time = time.time()
        sorted_array = algo(string_array)
        end_time = time.time()
        utilities.add_data(performanceData, i, algo.__name__, end_time-start_time)
        index_str = strVal.index(sorted_array[index2Check])
        print("Sorted arrays' element: ", sorted_array[index2Check], " at index: ", index2Check, " is at index: ", index_str, " in the original array")
        i+=1
    elif len(number_array) != 0:
        start_time = time.time()
        sorted_array = algo(number_array)
        end_time = time.time()
        utilities.add_data(performanceData, i, algo.__name__, end_time-start_time)
        print(numbVal)
        index_numb = numbVal.index(sorted_array[index2Check])
        print("Sorted arrays' element: ", sorted_array[index2Check], " at index: ", index2Check, " is at index: ", index_numb, " in the original array")
        i+=1
    else:
        pass

utilities.export2CSV(performanceData)