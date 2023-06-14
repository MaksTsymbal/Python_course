# Create a class method named `validate`, which should be called from the `__init__`
# method to validate parameter email, passed to the constructor. The logic inside the `validate`
# method could be to check if the passed email parameter is a valid email string.

import re


class User:
    def __init__(self, email):
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email address.")

valid_emails = []
invalid_emails = []

test_emails = [
    "user@example.com",   # valid email
    "user.example.com",   # missing @ symbol
    "user@.example.com",  # missing domain
    "user@example",       # missing top-level domain
    "user@example.c",     # invalid top-level domain
]

for email in test_emails:
    try:
        user = User(email)
        valid_emails.append(email)
    except ValueError:
        invalid_emails.append(email)

print("Valid emails:")
for email in valid_emails:
    print(email, "is a valid email.")

print("\nInvalid emails:")
for email in invalid_emails:
    print(email, "is an invalid email.")
