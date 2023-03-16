# task_2
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

input_number = input("Enter phone number:")
if len(input_number) != 10:
    print("Invalid phone number length")
elif not input_number.isdigit():
    print("Phone number must contain only digits")
else:
    print("Valid phone number")
