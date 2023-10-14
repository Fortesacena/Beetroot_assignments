#---------------------------TASK 1-----------------------------

"""
String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String
"""

input_string = input("Write a string:")

if len(input_string) < 2:
    print (" ")  #Empty String
else:
    first_two = input_string[:2]  # First two characters
    last_two = input_string[-2:]  # Last two characters
    print(first_two + last_two)


#---------------------------TASK 2-----------------------------
"""
The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The program should check
that the string contains only numerical characters and is only 10 characters long. Print a suitable message
depending on the outcome of the string evaluation.
"""

phone_number = input("Enter a 10-digit phone number: ")

if len(phone_number) == 10 and phone_number.isdigit():
    print("Valid phone number:", phone_number)
else:
    print("Invalid phone number.")

#---------------------------TASK 3-----------------------------
"""
The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

stored_name = "anton"


input_name = input("Enter your name: ")


if input_name.lower() == stored_name:
    print("Name matched.")
else:
    print("Name did not match.")

    
