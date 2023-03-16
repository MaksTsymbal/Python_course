# task_1
# Make a program that has your name and the current day of the week stored as separate variables and
# then prints a message like this:
#      "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.
#
# An additional bonus will be to use different string formatting methods for constructing result string.
name = "Maks"
day = "10.03.2023"
# using string concatenation
print("Good day " + name + "! " + day + " is a perfect day to learn some python.")
# using string interpolation
print(f"Good day {name}! {day} is a perfect day to learn some python.")
# using format method
print("Good day {}! {} is a perfect day to learn some python.".format(name, day))
# using format method with numbered placeholders
print("Good day {0}! {1} is a perfect day to learn some python.".format(name, day))
# using format method with named placeholders
print("Good day {n}! {d} is a perfect day to learn some python.".format(n=name, d=day))