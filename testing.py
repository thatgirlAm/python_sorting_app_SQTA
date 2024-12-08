import json
import csv
import bubble_sort as bs
import quick_sort as qs
import merge_sort as ms
# import sorter as rs
import radix_sort as rs


def run_tests(file):
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

            # Run the sorting algorithm
            actual_output = algorithms[algo](input_data[:])  # Pass a copy of the input
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


# Write results to a CSV file
def write_results_to_csv(results, output_file):
    fieldnames = ["id", "algorithm", "status", "score", "input", "expected_output", "actual_output", "test_description"]
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


# Main Function
if __name__ == "__main__":
    # Specify the test case file and output file
    output_file = "test_result.csv"

    # Run tests
    results = run_tests("test_cases.json")

    # Write results to CSV
    write_results_to_csv(results, output_file)

    print(f"Test results written to {output_file}")