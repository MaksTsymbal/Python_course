# task_2
# The “sys.path” list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python?
# If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
import sys
print(sys.path)
sys.path.append('C:\\Users\\Максим\\PycharmProjects\\my_modules')
print(sys.path)
# text in my_module.py
# def hello():
#     print('Hello from my_module!')
from my_module import hello
hello()