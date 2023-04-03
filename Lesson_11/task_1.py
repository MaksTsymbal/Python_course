# Write a Python program to detect the number of local variables declared in a function.
def my_function():
    x = 10
    y = 'hello'
    z = [1, 2, 3]
    print('Number of local variables in my_function:', len(locals()))


my_function()

