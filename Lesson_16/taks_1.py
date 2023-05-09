# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0. Tips: see the documentation for
# the enumerate function

def with_index(iterable, start=0):
    for i, item in enumerate(iterable, start=start):
        yield i, item

my_list = ['apple', 'banana', 'cherry', 'Maksik']
for index, value in with_index(my_list):
    print(f'{index}: {value}')

