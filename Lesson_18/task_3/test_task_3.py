from task_3 import process_file_data

def test_process_file_data(tmp_path):
    # Create a temporary file with some test data
    test_data = "abcdefg"
    test_file = tmp_path / "test.txt"
    with open(test_file, "w") as f:
        f.write(test_data)

    # Pass the file object to process_file_data and check the result
    with open(test_file, "r") as f:
        result = process_file_data(f)

    assert result == test_data[::-1]
