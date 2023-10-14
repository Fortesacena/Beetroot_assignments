
#---------------------------TASK 1-----------------------------
"""
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""

import random

numbers = []

count = 0
while count < 10:
    random_number = random.randint(1, 10)  
    numbers.append(random_number)
    count += 1

largest_number = numbers[0]
index = 1
while index < 10:
    if numbers[index] > largest_number:
        largest_number = numbers[index]
    index += 1

print("Random numbers:", numbers)
print("Largest number:", largest_number)


#---------------------------TASK 2-----------------------------
"""
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""

import random

list1 = []
list2 = []


count = 0
while count < 10:
    list1.append(random.randint(1, 10))  
    list2.append(random.randint(1, 10))
    count += 1

common_list = []

index1 = 0
while index1 < 10:
    element = list1[index1]
    if element in list2 and element not in common_list:
        common_list.append(element)
    index1 += 1

index2 = 0
while index2 < 10:
    element = list2[index2]
    if element in list1 and element not in common_list:
        common_list.append(element)
    index2 += 1

print("List 1:", list1)
print("List 2:", list2)
print("Common List:", common_list)

#---------------------------TASK 3-----------------------------

"""
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration.
"""

all_numbers = list(range(1, 101))

numbers = []

index = 0
while index < len(all_numbers):
    number = all_numbers[index]

    if number % 7 == 0 and number % 5 != 0:
        numbers.append(number)

    index += 1

print(numbers)
