# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0. Tips: see the documentation for
# the enumerate function

def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

my_list = ['apple', 'banana', 'cherry', 'Maksik']
for index, value in with_index(my_list):
    print(f'{index}: {value}')


