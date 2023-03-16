# task_3
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list.
# Finally, print the list.
# Constraint: use only while loop for iteration

numbers = []
i = 1
while i <= 100:
    numbers.append(i)
    i += 1
divisible_by_7_not_5 = []
i = 0
while i < len(numbers):
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        divisible_by_7_not_5.append(numbers[i])
    i += 1
print(divisible_by_7_not_5)
