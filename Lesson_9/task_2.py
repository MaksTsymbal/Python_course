# task_2
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).
def calculate_squared_divided():
    try:
        a = float(input("Enter a number for a: "))
        b = float(input("Enter a number for b: "))
        if b == 0:
            raise ZeroDivisionError("b cannot be zero!")
        return (a ** 2) / b
    except ValueError as e:
        print("Oops, one of the values you entered is not a number!")
        raise e


try:
    result = calculate_squared_divided()
    print("Result:", result)
except ZeroDivisionError as e:
    print("Oops, something went wrong:", e)
except ValueError as e:
    print("Oops, something went wrong:", e)


