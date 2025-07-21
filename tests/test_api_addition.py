import json
import pytest
import os


def add(a, b):
    return a + b

# Get the directory of the current file (tests/)
current_dir = os.path.dirname(__file__)

# Go up to sdet_framework/, then into data/
file_path = os.path.join(current_dir, "..", "data", "test_data.json")

# Convert to absolute path
file_path = os.path.abspath(file_path)

# Load JSON test data
with open(file_path, "r") as f:
    data = json.load(f)



# Convert to list of tuples
test_data = [(case["input"][0], case["input"][1], case["expected"]) for case in data["test_cases"]]

# Mark test function for pytest to run
@pytest.mark.parametrize("a, b, expected", test_data)
def test_addition(a, b, expected):
    result = add(a, b)
    assert result == expected
