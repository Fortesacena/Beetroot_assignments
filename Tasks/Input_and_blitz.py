
#---------------------------TASK 1-----------------------------
"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
The result should be sent back to the user via a print statement.

"""

import random

random_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == random_number:
    print("Congratulations! You guessed the correct number:", random_number)
else:
    print("Sorry, the correct number was:", random_number)


#---------------------------TASK 2-----------------------------
"""
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

"Hello <name>, on your next birthday you'll be <age+1> years"
"""

name = input("Enter your name:")
age = int(input("Enter your age:"))

print("Hello", name, ", on your next birthday you'll be" ,age+1, "years")

#---------------------------TASK 3-----------------------------
"""
Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters 
of the input string.

For example, the program obtained the word 'hello', so it should print 5 random strings(words) that 
combine characters 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …

Tips: Use random module to get random char from string)
"""

import random

input_string = input("Enter a string: ")

for x in range(5):
    random_string = ''.join(random.sample(input_string, len(input_string)))
    print(random_string)


#---------------------------TASK 4-----------------------------
"""
The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
and then responds with a message accordingly.
"""
import random

num1 = random.randint(1, 10)
num2 = random.randint(1,10)
operator = input("Enter the operator (+, -, *, /): ")

expression = f"{num1} {operator} {num2}"

if(operator == '+'):
    x=num1+num2

elif(operator == '-'):
    x=num1-num2

elif(operator == '*'):
    x=num1*num2

elif(operator == '/'):
    x=num1/num2

user_answer = float(input(f"What is {expression} equal to? "))
correct_answer = eval(expression)

if(user_answer==correct_answer):
    print("Correct!")
else:
    print("Wrong answer!")

