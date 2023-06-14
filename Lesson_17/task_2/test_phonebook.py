import unittest
from phonebook_manager import PhonebookManager
from phonebook import Phonebook

class TestPhonebookManager(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"first_name": "John", "last_name": "Doe", "phone_number": "123-456-7890", "city": "New York", "state": "NY"},
            {"first_name": "Jane", "last_name": "Doe", "phone_number": "456-789-0123", "city": "Boston", "state": "MA"}
        ]
        self.manager = PhonebookManager(self.data)

    def test_search_by_first_name(self):
        results = self.manager.search("first_name", "John")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["phone_number"], "123-456-7890")

    def test_search_by_last_name(self):
        results = self.manager.search("last_name", "Doe")
        self.assertEqual(len(results), 2)

    def test_search_by_full_name(self):
        results = self.manager.search("first_name", "John")
        self.assertEqual(len(results), 1)

        results = self.manager.search("last_name", "Doe")
        self.assertEqual(len(results), 2)

        results = self.manager.search("first_name", "John")
        self.assertEqual(len(results), 1)

    def test_search_by_phone_number(self):
        results = self.manager.search("phone_number", "123-456-7890")
        self.assertEqual(len(results), 1)

    def test_search_by_city_or_state(self):
        results = self.manager.search("city", "New York")
        self.assertEqual(len(results), 1)

        results = self.manager.search("state", "MA")
        self.assertEqual(len(results), 1)


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook("test_phonebook")

    def test_load_data(self):
        self.assertIsInstance(self.phonebook.data, list)

    def test_add_entry(self):
        original_length = len(self.phonebook.data)
        self.phonebook.add_entry()
        new_length = len(self.phonebook.data)
        self.assertEqual(new_length, original_length + 1)


if __name__ == '__main__':
    unittest.main()
