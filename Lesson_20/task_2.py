# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

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


def is_balanced_sequence(sequence):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != bracket_pairs[char]:
                return False

    return stack.is_empty()


sequence = input("Enter a sequence of characters: ")
if is_balanced_sequence(sequence):
    print("The sequence is balanced.")
else:
    print("The sequence is not balanced.")
