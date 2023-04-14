# Create your custom exception named `CustomException`, you can inherit from base Exception class,
#     but extend its functionality to log every error message to a file named `logs.txt`.
#     Tips: Use __init__ method to extend functionality for saving messages to file
class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'a') as f:
            f.write(msg + '\n')

try:
    x = int(input('Enter a number greater than 5: '))
    if x <= 5:
        raise CustomException(f'Number {x} is not greater than 5')
except CustomException as e:
    print(e.msg)
