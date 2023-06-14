# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method,
# which has to cover all the requirements to context managers mentioned here:
# Context Manager Types
# The with statement

import logging


class OpenFileManager:
    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)
        self.counter = 0
        self.logger = logging.getLogger('OpenFileManager')

    def __enter__(self):
        self.counter += 1
        self.logger.info(f'Opening file {self.file.name}, counter = {self.counter}')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.counter -= 1
        self.logger.info(f'Closing file {self.file.name}, counter = {self.counter}')
        self.file.close()
        if exc_type:
            self.logger.error(f'Exception {exc_type} occurred: {exc_value}')
            return False
        return True


with OpenFileManager('test.txt', 'a') as f1:
    with OpenFileManager('test.txt', 'a') as f2:
        f1.write('world!')
        f2.write('Hello,')