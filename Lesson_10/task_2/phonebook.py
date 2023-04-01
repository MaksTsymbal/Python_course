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
        print("Search entries:")
        print("1. By first name")
        print("2. By last name")
        print("3. By full name")
        print("4. By phone number")
        print("5. By city or state")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            first_name = input("Enter first name: ")
            results = self.manager.search_by_first_name(first_name)
            PhonebookEntry.display_search_results(results)
        elif choice == "2":
            last_name = input("Enter last name: ")
            results = self.manager.search_by_last_name(last_name)
            PhonebookEntry.display_search_results(results)
        elif choice == "3":
            full_name = input("Enter full name: ")
            results = self.manager.search_by_full_name(full_name)
            PhonebookEntry.display_search_results(results)
        elif choice == "4":
            phone_number = input("Enter phone number: ")
            results = self.manager.search_by_phone_number(phone_number)
            PhonebookEntry.display_search_results(results)
        elif choice == "5":
            city_or_state = input("Enter city or state: ")
            results = self.manager.search_by_city_or_state(city_or_state)
            PhonebookEntry.display_search_results(results)
        else:
            print("Invalid choice.")

    def delete_entry(self):
        phone_number = input("Enter phone number: ")
        if self.manager.delete_entry_by_phone_number(phone_number):
            print("Entry deleted successfully.")
            self.save_data()
        else:
            print("Entry not found.")

    def update_entry(self):
        phone_number = input("Enter phone number: ")
        results = self.manager.search_by_phone_number(phone_number)
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
            print("Phonebook options:")
            print("1. Add new entry")
            print("2. Search entries")
            print("3. Delete an entry")
            print("4. Update an entry")
            print("5. Exit")
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


