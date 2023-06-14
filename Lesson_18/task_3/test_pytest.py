import pytest
import os
from task_2 import OpenFileManager
from task_3 import process_file_data

@pytest.fixture
def file_obj(tmp_path):
    # Create a temporary file with some test data
    test_data = "abcdefg"
    test_file = tmp_path / "test.txt"
    with open(test_file, "w") as f:
        f.write(test_data)

    # Return a file object using our context manager
    with OpenFileManager(test_file) as f:
        yield f

    # Clean up the temporary file
    os.remove(test_file)

def test_process_file_data_with_fixture(file_obj):
    # Pass the file object to process_file_data and check the result
    result = process_file_data(file_obj)
    assert result == "abcdefg"[::-1]
