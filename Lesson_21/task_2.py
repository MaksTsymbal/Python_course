# Implement a stack using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack.")
        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

stack = LinkedListStack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.size())  # Output: 3
print(stack.peek())  # Output: 30

item = stack.pop()
print(item)  # Output: 30

print(stack.size())  # Output: 2
