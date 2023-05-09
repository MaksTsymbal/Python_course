# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class MyIterable:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration
        else:
            result = self.values[self.index]
            self.index += 1
            return result

    def __getitem__(self, index):
        return self.values[index]

    def generator(self):
        for value in self.values:
            yield value


iterable = MyIterable([1, 2, 3, 4, 5])

# Using for-in loop with generator
for value in iterable.generator():
    print(value)  # 1 2 3 4 5



