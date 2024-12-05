# this is the utilities files for functions we might need to use several times


# this function aims to select a particular digit of an element
def number_digits(element, digit, max_digits):
    element_str = str(element).zfill(max_digits)
    return int(element_str[digit])



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

#print(key_finder(45, {0:45, 29:478, 3:23}))

def test(L):
    L.remove(1)
    return L

