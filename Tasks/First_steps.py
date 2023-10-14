
#********************** 2) FIRST STEPS*************************

#---------------------------TASK 2-----------------------------

#Create a python program named “task2”, and use the built-in function `print` in it several times. 
#Try to pass “sep”, “end” params and pass several parameters separated by commas. 
#Also, provide a comment text above each print statement, mentioned above, with the expected output
# after execution of the particular print statement.

# Sep parameter
print("This", "is", "a", "sample", "output", sep="-")
# Expected Output: This-is-a-sample-output

# End parameter
print("Hello, ", end="")
print("world!")
# Expected Output: Hello, world!

# Using both sep and end
print("Apples", "Bananas", "Cherries", sep=", ", end=" are delicious!\n")
# Expected Output: Apples, Bananas, Cherries are delicious!



# Multiple parameters separated by commas
name = "Fortesa"
age = 21
city = "Rahovec"
print("Name:", name, "Age:", age, "City:", city)
# Expected Output: Name: Fortesa Age: 21 City: Rahovec


#---------------------------TASK 3-----------------------------

# Write a program, which has two print statements to print the following text 
# (capital letters "O" and "H", made from "#" symbols):


# Printing the letter "O" using \n and \t
print("#####\n#\t#\n#\t#\n#\t#\n#\t#\n#\t#\n#####")


# Printing the letter "H" using \n and \t
print("#\t#\n#\t#\n#####\n#\t#\n#\t#\n#\t#")
