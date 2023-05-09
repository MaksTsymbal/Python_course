import logging
import unittest
from io import StringIO
import os
from task_2 import OpenFileManager


class TestOpenFileManager(unittest.TestCase):

    def test_file_opened_successfully(self):
        # Arrange
        filename = 'test.txt'
        with open(filename, 'w') as f:
            f.write('test')

        # Act
        with OpenFileManager(filename) as f:
            contents = f.read()

        # Assert
        self.assertEqual(contents, 'test')

        # Clean up
        os.remove(filename)

    def test_file_not_found(self):
        # Arrange
        filename = 'non_existent_file.txt'

        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            with OpenFileManager(filename):
                pass

    def test_file_closed_after_exception(self):
        # Arrange
        filename = 'test.txt'
        with open(filename, 'w') as f:
            f.write('test')

        # Act & Assert
        try:
            with OpenFileManager(filename) as f:
                raise Exception('Test exception')
        except Exception as e:
            self.assertEqual(str(e), 'Test exception')

        self.assertTrue(f.closed)

        # Clean up
        os.remove(filename)

    def test_logging(self):
        # Arrange
        filename = 'test.txt'
        with open(filename, 'w') as f:
            f.write('test')
        log_stream = StringIO()
        logger = logging.getLogger('OpenFileManager')
        handler = logging.StreamHandler(log_stream)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Act
        with OpenFileManager(filename) as f:
            pass

        # Assert
        self.assertEqual(log_stream.getvalue().strip(),
                         'Opening file test.txt, counter = 1\n'
                         'Closing file test.txt, counter = 0')

        # Clean up
        os.remove(filename)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
