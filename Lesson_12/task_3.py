# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.
#
# def arg_rules(type_: type, max_length: int, contains: list):
#     pass
#
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
#
# assert create_slogan('johndoe05@gmail.com') is False
#
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Error: Argument {arg} is not of type {type_}")
                    return False
                if len(arg) > max_length:
                    print(f"Error: Argument {arg} exceeds the maximum length of {max_length}")
                    return False
                if not all(symbol in arg for symbol in contains):
                    print(f"Error: Argument {arg} does not contain all symbols {contains}")
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!')
print(create_slogan(5))