# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def multiply_by(x):
    def multiplier(y):
        return x * y
    return multiplier


# Create a function that multiplies by 3
triple = multiply_by(3)

# Create a function that multiplies by 5
quintuple = multiply_by(5)

# Use the functions to multiply numbers
print(triple(10))    # Output: 30
print(quintuple(4))  # Output: 20
