# Take your implementation of the context manager class from Task 1 and write tests for it.
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
# And also, write tests when your class raises errors or you have errors in the runtime context suite.

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