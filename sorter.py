# this is the sorter file

import utilities
def radix_number(array):
    str_array = []
    dictionary = utilities.dictionary(array)
    output_array = []

    # transforming numbers in strings to access the digits and populating the output array
    for element in array:
        str_array.append(str(element))
        output_array.append(element)

    max_digits = len(str_array[0])

    # getting the highest number of digits in the array :max_digits
    for element in str_array:
        if len(element) > max_digits:
            max_digits = len(element)

    # initiating loops for radix sorting
    for i in range(max_digits):
        temp_output = []
        for element in output_array:
            inserted = False

            # getting the digits
            for j, other_element in enumerate(temp_output):
                digit_element = utilities.number_digits(element, -(i + 1), max_digits)
                digit_other = utilities.number_digits(other_element, -(i + 1), max_digits)

                # comparison and appending digits in temporary array
                if digit_element < digit_other:
                    temp_output.insert(j, element)
                    inserted = True
                    break
            # inserting the bigger digit
            if not inserted:
                temp_output.append(element)
        output_array = temp_output

    return output_array, dictionary

print(radix_number([234,4567,33, 33, 123849505, 5673, 2]))

