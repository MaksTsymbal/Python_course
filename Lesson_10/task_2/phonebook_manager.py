# This module defines the PhonebookManager class,
# which manages the phonebook entries. It contains methods for adding,
# searching, updating, and deleting entries.

class PhonebookManager:
    def __init__(self, data):
        self.data = data

    def search(self, field, value):
        return [entry for entry in self.data if entry[field] == value]

    def delete_entry_by_phone_number(self, phone_number):
        for entry in self.data:
            if entry["phone_number"] == phone_number:
                self.data.remove(entry)
                return True
        return False

    def update_entry_by_phone_number(self, phone_number, updated_entry):
        for index, entry in enumerate(self.data):
            if entry["phone_number"] == phone_number:
                self.data[index] = updated_entry.to_dict()
                return True
        return False



