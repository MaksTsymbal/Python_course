# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_print():
    stack = Stack()
    sequence = input("Enter a sequence of characters: ")

    # Push each character onto the stack
    for char in sequence:
        stack.push(char)

    reversed_sequence = ""

    # Pop characters from the stack and build the reversed sequence
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    print("Reversed sequence:", reversed_sequence)


reverse_print()

