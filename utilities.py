# ---------- This is the utilities files for functions we might need to use several times ---------- #

# GLOBALS
LETTERS_RANKING = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
# option to be careful about special character "-"
LETTERS_RANKING["-"] = 27


# this function aims to select a particular digit of an element
def number_digits(element, digit, max_digits):
    element_str = str(element).zfill(max_digits)
    return int(element_str[digit])

# this function gets the max digit in an array
def max_digit(array):
    str_array = []
    for element in array:
        str_array.append(str(element))
    max_digits = len(str_array[0])

    # getting the highest number of digits in the array :max_digits
    for element in str_array:
        if len(element) > max_digits:
            max_digits = len(element)
    return max_digits


# this function was created to fill the gap from the least significant to the biggest element and return the leter
def fill_strings(element, max_length, index):
    strings = element.zfill(max_length+1)
    strings = strings.lower()
    return strings[index]


# this function creates a dictionary for each input array to remember the position of each element
def dictionary(array):
    array_dictionary = {}
    for i in range(len(array)):
        array_dictionary[i] = array[i]
    return array_dictionary

# this function is a value finder for a dictionary
def key_finder(value, dictionary):
    for k, v in dictionary.items():
        if v == value:
            return k
    return -1

# second way to find keys
def key_finder_2(char, ranking):
    return ranking.get(char, -1)


