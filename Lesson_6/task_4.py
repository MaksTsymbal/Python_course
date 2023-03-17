# task_4
# Create an email with the days of the week.
# In one line (or as usual) create a dictionary of the form: {1: "Monday", 2:...
# Also, in one line or as usual, create a reverse dictionary {"Monday": 1,

days_email = "Here are the days of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday."
days_dict = {i+1: day for i, day in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
reverse_days_dict = {day: i+1 for i, day in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
print(days_email)
print(days_dict)
print(reverse_days_dict)
