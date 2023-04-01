# This module defines the PhonebookEntry class, which represents a single entry in the phonebook.
# It contains methods for creating an entry from user input, displaying search results,
# and converting an entry to a dictionary.

class PhonebookEntry:
    def __init__(self, first_name, last_name, phone_number, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.city = city
        self.state = state

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "city": self.city,
            "state": self.state
        }

    def display(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Phone: {self.phone_number}")
        print(f"Location: {self.city}, {self.state}")

    @staticmethod
    def create_entry_from_user_input():
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        return PhonebookEntry(first_name, last_name, phone_number, city, state)

    @staticmethod
    def display_search_results(results):
        if results:
            for index, entry_dict in enumerate(results, start=1):
                entry = PhonebookEntry(**entry_dict)
                print(f"{index}.")
                entry.display()
                print()
        else:
            print("No results found.")


