# Library/main.py

"""Entry point for this library, responsible to allow initialising of input array, execution of sorting algoritms and validation of their logic.

The module contains the following functions:

- `enterData()` - Returns an array of user entered data.
- `generateStringData()` - Returns an array containing string data of size specified by the user.
- `generateNumberData()` - Returns an array containing number data of size specified by the user.
"""

from tkinter import WORD
import bubble_sort as bs
import quick_sort as qs
import merge_sort as ms
import radix_sort as rs
import time
import utilities
import re


performanceData = []
ncr = []
scr = []
numbDict = {}
strDict = {}

def enterData():

    """Create an array of user entered data.

    Returns:
        Return arrays of either string or number data.
    """

    user_data_input = input("Enter elements separated by spaces (mix of numbers and strings): ").split()
    number_array = []
    string_array = []
    for item in user_data_input:

        if(item.isdigit()):
            number_array.append(item)
        elif not (bool(re.search(r'[^A-Za-z0-9]', item))):
            string_array.append(item)
        else:
            pass

    return number_array, string_array

def generateStringData():

    """Produce automatically an array of user specified size and containing strings of varied size.

    Returns:
        Return a string array.
    """

    dataSize = int(input("Enter the size of string array to be generated: "))
    string_array = utilities.generate_StringArray(dataSize)
    return string_array

def generateNumberData():

    """Produce automatically an array of user specified size and containing random numbers.

    Returns:
        Return a number array.
    """

    dataSize = int(input("Enter the size of number array to be generated: "))
    number_array = utilities.generate_numberArray(dataSize)
    return number_array

user_input = int(input("Enter 1 to enter input array or Enter 2 to auto-generate string input arrays or Enter 3 to auto-generate number input arrays: "))

if user_input == 1:
    number_array, string_array = enterData()
    scr = string_array
    ncr = number_array
elif user_input == 2:
    string_array = generateStringData()
    scr = string_array
    number_array = []
elif user_input == 3:
    number_array = generateNumberData()
    ncr = number_array
    string_array = []
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