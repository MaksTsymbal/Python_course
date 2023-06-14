# Extend UnorderedList
# Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method,
# which will take two parameters `start` and `stop`, and return a copy of the list starting at the position
# and going up to but not including the stop position.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"Item '{item}' not found in the list.")

    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty list.")
        if pos is None or pos == self.size() - 1:
            return self.pop_last()
        elif pos == 0:
            return self.pop_first()
        else:
            return self.pop_position(pos)

    def pop_last(self):
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        if previous is None:
            self.head = None
        else:
            previous.next = None
        return current.data

    def pop_first(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty list.")
        data = self.head.data
        self.head = self.head.next
        return data

    def pop_position(self, pos):
        if pos < 0 or pos >= self.size():
            raise IndexError("Invalid position.")
        current = self.head
        previous = None
        index = 0
        while index < pos:
            previous = current
            current = current.next
            index += 1
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        return current.data

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError("Invalid position.")
        if pos == 0:
            self.add(item)
        else:
            new_node = Node(item)
            current = self.head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.next
                index += 1
            previous.next = new_node
            new_node.next = current

    def slice(self, start, stop):
        if start < 0 or start >= self.size() or stop <= start or stop > self.size():
            raise IndexError("Invalid slice parameters.")
        new_list = UnorderedList()
        current = self.head
        index = 0
        while index < start:
            current = current.next
            index += 1
        while index < stop:
            new_list.append(current.data)
            current = current.next
            index += 1
        return new_list


# Example usage of the extended UnorderedList class
my_list = UnorderedList()
my_list.add(10)
my_list.add(20)
my_list.add(30)

my_list.append(40)
print(my_list.size())  # Output: 4

print(my_list.index(30))  # Output: 2

print(my_list.pop())  # Output: 40

my_list.insert(1, 25)
print(my_list.pop(1))  # Output: 25

sliced_list = my_list.slice(1, 3)
current = sliced_list.head
while current is not None:
    print(current.data)
    current = current.next
