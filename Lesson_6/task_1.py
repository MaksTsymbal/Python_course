# task_1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as
# keys and the number of occurrences as values.

sentence = input("Inpute the sentence: ")
words = sentence.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)

