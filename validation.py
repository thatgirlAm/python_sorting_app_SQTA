# SQTA and RASD Assignment : python sorting library
# Amaelle DIOP (461543) - Mansher Gill(448666) 

# this is the validation file, it maanges validation of the input data 


# validation for size
def size(array):
    return 0<len(array)<1000000

# validation for type
def type(array):
    for element in array:
        if not isinstance(element, (str, float)):
            return False
    return True