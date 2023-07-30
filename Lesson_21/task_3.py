# Implement a queue using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue.")
        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

queue = LinkedListQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.size())  # Output: 3
print(queue.peek())  # Output: 10

item = queue.dequeue()
print(item)  # Output: 10

print(queue.size())  # Output: 2
