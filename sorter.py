# this is the sorter file

import utilities
def radix_number(array):
    max_digits = utilities.max_digit(array)
    dictionary = utilities.dictionary(array)
    output_array = []

    # populating the output array
    for element in array:
        output_array.append(element)

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

def radix_string(array):
    dictionary = utilities.dictionary(array)
    output_array = array.copy()
    max_length = utilities.max_digit(array)

    for i in range(max_length):
        temp_output = []
        for element in output_array:
            inserted = False

            # comparison and changing position
            for j, other in enumerate(temp_output):
                letter_element = utilities.fill_strings(element.lower(), max_length, -i - 1)
                letter_other = utilities.fill_strings(other.lower(), max_length, -i - 1)
                if utilities.key_finder_2(letter_element, utilities.LETTERS_RANKING) < utilities.key_finder_2(letter_other, utilities.LETTERS_RANKING):
                    temp_output.insert(j, element)
                    inserted = True
                    break

            if not inserted:
                temp_output.append(element)

        output_array = temp_output
    return output_array, dictionary



# Examples

print(radix_string(["sa", "sal067ut", "argente", "Ifeu", "as" ,"jirejguhirgbdhsifbzejdcn"]))
print(radix_number([234,4567,33, 33, 123849505, 5673, 2]))

