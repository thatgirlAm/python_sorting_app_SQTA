import json
import csv
import sorter
import bubble_sort
import merge_sorter
import quick_sort



# Step 1: Define the function to load test cases
def load_test_cases(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)


# Step 2: Run the tests
def run_tests(test_cases):
    results = []
    algorithms = {
        "merge_sort": merge_sort,
        "radix_sort": radix_sort,
        "quicksort": quicksort,
        "bubble_sort": bubble_sort
    }

    for test in test_cases:
        test_id = test["id"]
        input_data = test["input"]
        expected_output = test["expected_output"]
        algorithm_name = test["algorithm"]

        if algorithm_name not in algorithms:
            result = {
                "id": test_id,
                "algorithm": algorithm_name,
                "status": "FAIL",
                "score": 0,
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": "Algorithm not found"
            }
        else:
            # Run the sorting algorithm
            actual_output = algorithms[algorithm_name](input_data[:])  # Pass a copy of the input
            status = "PASS" if actual_output == expected_output else "FAIL"
            score = 1 if status == "PASS" else 0

            result = {
                "id": test_id,
                "algorithm": algorithm_name,
                "status": status,
                "score": score,
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": actual_output
            }

        results.append(result)

    return results


# Step 3: Write results to a CSV file
def write_results_to_csv(results, output_file):
    fieldnames = ["id", "algorithm", "status", "score", "input", "expected_output", "actual_output"]
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


# Main Function
if __name__ == "__main__":
    # Specify the test case file and output file
    json_file = "test_cases.json"  # Replace with your JSON file path
    output_file = "test_results.csv"

    # Load test cases
    test_cases = load_test_cases(json_file)

    # Run tests
    results = run_tests(test_cases)

    # Write results to CSV
    write_results_to_csv(results, output_file)

    print(f"Test results written to {output_file}")