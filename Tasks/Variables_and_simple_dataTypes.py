#---------------------------TASK 1-----------------------------
"""
The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:  

"Good day <name>! <day> is a perfect day to learn some python."
Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.
"""

name = "Fortesa"
day = "10/14/2023"

print('Good day', name , '!', day, 'is a perfect day to learn some python.')


#---------------------------TASK 2-----------------------------
"""
Manipulate strings.

Save your first and last name as separate variables, then use string concatenation
to add them together with a white space in between and print a greeting.
"""

name1 = "Fortesa"
Surname = "Cena"

#Concatination
full_name = name + " " + Surname
print("Hello", full_name, "!")

#---------------------------TASK 3-----------------------------
"""
Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""

# Define two numbers
a = 10
b = 3

# Addition
addition_result = a + b
print("Addition:", addition_result)

# Subtraction
subtraction_result = a - b
print("Subtraction:", subtraction_result)

# Division
division_result = a / b
print("Division:", division_result)

# Multiplication
multiplication_result = a * b
print("Multiplication:", multiplication_result)

# Exponentiation
exponent_result = a ** b
print("Exponentiation:", exponent_result)

# Modulus 
modulus_result = a % b
print("Modulus:", modulus_result)

# Floor Division 
floor_division_result = a // b
print("Floor Division:", floor_division_result)
