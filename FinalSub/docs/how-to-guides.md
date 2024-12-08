This part of the project documentation focuses on a
**problem-oriented** approach. The following data is
like an introduction to the application.

## How To Execute this Library?

In order to use this library, download the file named
FinalSub and once it is done, open a terminal in the
downloaded files' location and run the following commands
to run the code documentation part.

To Sort Array - "python main.py"

To Run Test Cases - "python testing.py"


## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        how-to-guides.md  # This is a how-to-page to allow a user to use this library.
        explanation.md  # This page provide explanation of each module and constituting functions.
    Library/
        bubble_sort.py  # This file is for bubble sort algorithm logic
        main.py  # This is the main file which will implement this library
        merge_sort.py  # This file is for merge sort algorithm logic
        quick_sort.py  # This file is for quick sort algorithm logic
        radix_sort.py  # This file is for radix sort algorithm logic
        testing.py  # This file runs tests over all algorithms
        test_cases.json  # This file mentions the test cases to execute
        utilities.py  # This file contains additional functions required
        __init__.py  # This is a basic file for code documentation


Inside Library directory `main.py` is the main 
function that will execute the entire library
operations from the `Library.main`
module. Here the user can choose whether they
want to specify the array elements or whether
they want to proceed with auto generated arrays
where they can choose the array size. Also, 
this file will export the execution time of
each algorithm for performance comparison in
a file named execution_time.csv.

Inside Library directory `testing.py` is the 
module that will execute all test cases as
mentioned in `test_cases.json`, test results
will be exported as a csv file which is named 
test_result.csv and will be in the same directory.