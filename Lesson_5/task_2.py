# task_2
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
list1 = []
i = 0
while i < 10:
    list1.append(random.randint(1, 10))
    i += 1
list2 = []
i = 0
while i < 10:
    list2.append(random.randint(1, 10))
    i += 1
common = []
i = 0
while i < 10:
    if list1[i] in list2 and list1[i] not in common:
        common.append(list1[i])
    i += 1
print("List 1:", list1)
print("List 2:", list2)
print("Common integers:", common)
