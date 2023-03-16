# task_3
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.

import random
first_number = random.randint(0, 10)
second_number = random.randint(0, 10)
expression = int(input(f"What is the value of {first_number} + {second_number}? "))
if expression == (first_number + second_number):
    print("Correct!")
else:
    print("Incorrect.")