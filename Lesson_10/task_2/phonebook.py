# This module is the main module of the application that contains the user interface
# and the main logic of the phonebook application. It calls the other modules to perform specific tasks
# such as adding, searching, updating, and deleting entries.

import json
import os
from phonebook_entry import PhonebookEntry
from phonebook_manager import PhonebookManager


def dict_to_list(d):
    return list(d.values())


class Phonebook:

    GREETINGS = "Phonebook options:\n1. Add new entry\n2. Search entries\n3. Delete an entry\n4. Update an entry\n5. Exit"
    SEARCHING = "Search entries:\n1. By first_name\n2. By last_name\n3. By full_name\n4. By phone_number\n5. By city or state"
    FIELDS = list(('first_name', 'last_name', 'phone_number', 'city', 'state'))

    def __init__(self, name):
        self.name = name
        self.data = self.load_data()
        self.manager = PhonebookManager(self.data)

    def load_data(self):
        if os.path.exists(f"{self.name}.json"):
            with open(f"{self.name}.json", "r") as file:
                return json.load(file, object_hook=dict_to_list)
        else:
            raise FileNotFoundError(f"{self.name}.json not found.")

    def save_data(self):
        with open(f"{self.name}.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def add_entry(self):
        entry = PhonebookEntry.create_entry_from_user_input()
        self.data.append(entry.to_dict())
        print("New entry added successfully.")
        self.save_data()

    def search_entries(self):
        print(self.SEARCHING)
        field = input("Enter your entry: ")
        if field in self.FIELDS:
            value = input(f"Enter value for {field}: ")
            results = self.manager.search(f'{field}', value)
            PhonebookEntry.display_search_results(results)
        else:
            print("Invalid entry")


    def delete_entry(self):
        phone_number = input("Enter phone number: ")
        if self.manager.delete_entry_by_phone_number(phone_number):
            print("Entry deleted successfully.")
            self.save_data()
        else:
            print("Entry not found.")

    def update_entry(self):
        phone_number = input("Enter phone number: ")
        results = self.manager.search('phone_number', phone_number)
        if results:
            entry_dict = results[0]
            entry = PhonebookEntry(**entry_dict)
            entry.display()
            print("Enter updated information:")
            updated_entry = PhonebookEntry.create_entry_from_user_input()
            self.manager.update_entry_by_phone_number(phone_number, updated_entry)
            print("Entry updated successfully.")
            self.save_data()
        else:
            print("Entry not found.")

    def run(self):
        while True:
            print(self.GREETINGS)
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.search_entries()
            elif choice == "3":
                self.delete_entry()
            elif choice == "4":
                self.update_entry()
            elif choice == "5":
                self.save_data()
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


