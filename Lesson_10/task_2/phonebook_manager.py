# This module defines the PhonebookManager class,
# which manages the phonebook entries. It contains methods for adding,
# searching, updating, and deleting entries.

class PhonebookManager:
    def __init__(self, data):
        self.data = data

    def search_by_first_name(self, first_name):
        return [entry for entry in self.data if entry["first_name"] == first_name]

    def search_by_last_name(self, last_name):
        return [entry for entry in self.data if entry["last_name"] == last_name]

    def search_by_full_name(self, full_name):
        return [entry for entry in self.data if f"{entry['first_name']} {entry['last_name']}" == full_name]

    def search_by_phone_number(self, phone_number):
        return [entry for entry in self.data if entry["phone_number"] == phone_number]

    def search_by_city_or_state(self, city_or_state):
        return [entry for entry in self.data if entry["city"] == city_or_state or entry["state"] == city_or_state]

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



