# Create a simple function, which performs any logic of your choice with text data,
# which it obtains from a file object, passed to this function ( def test(file_obj) ).
# Create a test case for this function using pytest library (Full pytest documentation).
# Create pytest fixture, which uses your implementation of the context manager to return
# a file object, which could be used inside your function.

def process_file_data(file_obj):
    """Read data from a file object and return the reversed string."""
    data = file_obj.read()
    return data[::-1]
