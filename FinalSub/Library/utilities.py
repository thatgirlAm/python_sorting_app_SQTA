# Library/utilities.py

"""Provide several secondary function declarations.

This module contains supporting operational functions that are common across different modules.

The module contains the following functions:

- `number_digits(a, b, c)` - Selects a random number from a user entered number.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

import csv
import random
import string
LETTERS_RANKING = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
LETTERS_RANKING["-"] = 27


def number_digits(element, digit, max_digits):

    """Get individual digits from a number.

    Args:
        element: Entered large number
        digit: particular digit of choice
        max_digits: max digits to be checked

    Returns:
        Return particular digit from a number.
    """

    element_str = str(element).zfill(max_digits)
    return int(element_str[digit])

def max_digit(array):

    """Get the maximum digit in an array.

    Args:
        array: Array from which the max digit is to be found

    Returns:
        Return maximum digit in an array.
    """

    str_array = []
    for element in array:
        str_array.append(str(element))
    max_digits = len(str_array[0])

    # getting the highest number of digits in the array :max_digits
    for element in str_array:
        if len(element) > max_digits:
            max_digits = len(element)
    return max_digits

def fill_strings(element, max_length, index):

    """Fills gap from least significant to the largest element in the input.

    Args:
        element: Entered large number.
        max_length: max length of gap to fill
        index: particular index in the array

    Returns:
        Return the index of the gap.
    """

    strings = element.zfill(max_length+1)
    strings = strings.lower()
    return strings[index]

def dictionary(array):

    """Creates a dictionary for each input array to remember the position of each element

    Args:
        array: Input array.
        
    Returns:
        Return the index of the gap.
    """

    array_dictionary = {}
    for i in range(len(array)):
        array_dictionary[i] = array[i]
    return array_dictionary

def key_finder(value, dictionary):

    """To find value within a dictionary

    Args:
        value: Value to find within the dictionary.
        dictionary: The dictionary that is to be searched
        
    Returns:
        Return -1.
    """

    for k, v in dictionary.items():
        if v == value:
            return k
    return -1

def key_finder_2(char, ranking):
    """To find keys within a dictionary

    Args:
        char: Key to find within the dictionary.
        ranking: The index of the value to find.
        
    Returns:
        Return the index of the searched element.
    """
    return ranking.get(char, -1)

def generate_random_word(length=5):

    """To generate random words of length = 5

    Args:
        length: Length of the word to be generated.
        
    Returns:
        Return the word generated.
    """

    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_StringArray(dSize):

    """To generate array containing string elements of user-defined length

    Args:
        dSize: size of the array to be generated.
        
    Returns:
        Return the generated array.
    """

    return [generate_random_word(random.randint(3, 10)) for _ in range(dSize)]

def generate_numberArray(dSize):

    """To generate array containing number elements of user-defined length

    Args:
        dSize: size of the array to be generated.
        
    Returns:
        Return the generated array.
    """

    return [random.randint(0, 1000000) for _ in range(dSize)]

def add_data(data, index, element, extime):

    """To generate row form of data for the performance test for each algorithm.

    Args:
        data: Row data.
        index: Index of performance test being recorded
        element: Algorithm name
        extime: Time taken for algorithm to run
        
    Returns:
        Return the generated row data.
    """

    data.append({"Index": index, "Sorting Algo": element, "Execution Time": extime})

def export2CSV(rowData):
    
    """To export row form of data for the performance test for each algorithm into a csv file.

    Args:
        rowData: Row data.
        
    Returns:
        Create a .csv file and add the generated row data to .csv file.
    """

    with open("execution_time.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Index", "Sorting Algo", "Execution Time"])
        writer.writeheader()
        writer.writerows(rowData)

    print("Performance Data has been exported to data.csv")

def createRecord(arrayDict, arrayStart):

    """To generate a copy of the entered string or number array in form of a dictionary to track original index of elements in sorted arrays.

    Args:
        arrayDict: Dictionary name to be created.
        arrayStart: Initial user defined array.
        
    Returns:
        Return the generated row data.
    """

    for i in range(len(arrayStart)):
        arrayDict[i] = arrayStart[i]
    return arrayDict

