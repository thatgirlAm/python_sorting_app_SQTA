# Library/testing.py

"""Provides testing functionality for each algorithm over the input they get and the output they give.

The module contains the following functions:

- `run_tests(a)` - Reads a json file and runs these tests on each sorting algorithm to validate and verify them.
- `write_results_to_csv(a, b)` - Exports an input array to the mentioned file.
"""

import json
import csv
import bubble_sort as bs
import quick_sort as qs
import merge_sort as ms
import radix_sort as rs


def run_tests(file):

    """Read tests from a file and run them over an array of input processing them via different algorithms.

    Args:
        file: A file which contains JSON data related to the tests to be conducted and outputs the test results.

    Returns:
        Return test results in a managed format.
    """

    results = []
    algorithms = {
        "Merge Sort": ms.merge_sort,
        "Radix Sort": rs.radix_sort,
        "Quick Sort": qs.quick_sort,
        "Bubble Sort": bs.bubble_sort
    }
    for algo in algorithms.keys():
        with open(file, "r") as ffile:
            test_data = json.load(ffile)

        for i, test in enumerate(test_data["test_cases"], start=1):
            test_id = test["id"]
            input_data = test["input"]
            expected_output = test["expected"]
            description = test["description"]

            actual_output = algorithms[algo](input_data[:]) 
            status = "PASS" if actual_output == expected_output else "FAIL"
            score = 1 if status == "PASS" else 0

            result = {
                "id": test_id,
                "algorithm": algo,
                "status": status,
                "score": score,
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": actual_output,
                "test_description": description
            }
            results.append(result)

    return results


def write_results_to_csv(results, output_file):

    """Output test results to a .csv file.

    Args:
        results: Input test result data.
        output_file: A file to which test results are to be exported.

    Returns:
        Return test results in a managed format.
    """

    fieldnames = ["id", "algorithm", "status", "score", "input", "expected_output", "actual_output", "test_description"]
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


if __name__ == "__main__":
    output_file = "test_result.csv"
    results = run_tests("test_cases.json")
    write_results_to_csv(results, output_file)
    print(f"Test results written to {output_file}")