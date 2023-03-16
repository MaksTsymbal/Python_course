# task_1
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random
numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(1, 100))
    i += 1
largest = numbers[0]
i = 1
while i < 10:
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print("List of random numbers:", numbers)
print("Largest number:", largest)
