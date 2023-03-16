# task_3
# Create a program that reads an input string and then creates and prints 5
# random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

import random
word = input("Enter string: ")
characters = list(word)
for i in range(5):
    random_characters = random.sample(characters, len(characters))
    random_word = ''.join(random_characters)
    print(random_word)