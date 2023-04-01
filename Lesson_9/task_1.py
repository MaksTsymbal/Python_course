# task_1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?
def oops():
    raise IndexError("Oops, something went wrong!")

def call_oops():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")

def oops_1():
    raise KeyError("Oops, something went wrong!")
def call_oops_1():
    try:
        oops_1()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except KeyError as e:
        print(f"Caught a KeyError: {e}")

