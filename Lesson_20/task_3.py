# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order. Consider the case in which the element is not found -
# raise ValueError with proper info Message

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

    def get_from_stack(self, element):
        temp_stack = Stack()
        found = False

        # Search for the element in the stack
        while not self.is_empty():
            item = self.pop()
            if item == element:
                found = True
                break
            temp_stack.push(item)

        # Restore the original order of other elements in the stack
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the stack.")


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, element):
        found = False

        # Search for the element in the queue
        for i in range(len(self.items)):
            if self.items[i] == element:
                found = True
                break

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the queue.")


# Example usage of the extended Stack and Queue classes
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

try:
    print(stack.get_from_stack(20))  # Found in the stack, will print 20
    print(stack.get_from_stack(50))  # Not found in the stack, will raise ValueError
except ValueError as e:
    print(e)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

try:
    print(queue.get_from_queue(20))  # Found in the queue, will print 20
    print(queue.get_from_queue(50))  # Not found in the queue, will raise ValueError
except ValueError as e:
    print(e)
