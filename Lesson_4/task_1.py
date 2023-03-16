# task_1
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random
rand_number = random.randint(1, 10)
guess_answer = int(input("Enter a number from 1 to 10: "))
if guess_answer == rand_number:
    print("Congratulations! You guessed the number!")
else:
    print("Unfortunately, you were wrong. The guessed number was:", rand_number)