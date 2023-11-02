#---------------------------TASK 1-----------------------------

""" 
Imports practice

Make a directory with 2 modules; make a function in one of them; then import this function 
in the other module and use that in your script of choice.
"""
from module1 import convertToFahrenheit, convertToCelsius
print(convertToCelsius(35))
print(convertToFahrenheit(20))


#---------------------------TASK 2-----------------------------
"""
The sys module. 

The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible
to change it from within Python? If so, does it affect where Python looks for module files? 
Run some interactive tests to find it out.
"""
# sys.path consists of a list of directories where Python searches for modules.
#Yes, it is possible to change it from within Python.
#When you append a new directory to sys.path, you are essentially telling Python to include
#that directory in its search path for modules, so modifying sys.path from within Python 
# does affect where Python looks for module files.
import sys

print("Original sys.path:")
print(sys.path)

# Add the current directory to sys.path
new_path = r'C:\Users\forte\Desktop\Beetroot_course\Tasks\Modules_directory'
sys.path.append(new_path)

# Display the modified sys.path
print("\nModified sys.path:")
print(sys.path)

# Attempt to import a module after modifying sys.path
try:
    import module1 
    print("Module imported successfully.")
except ImportError:
    print("Module not found.")

# Remove the newly added path from sys.path
sys.path.remove(new_path)


print("\nsys.path after removing the added path:")
print(sys.path)




#---------------------------TASK 3-----------------------------
"""
Basics, import, work with os module

Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, for additional 
info about it follow the link or in case you have macOS or Linux - just call manual for this utility via 
command: man wc).

Create a Python module called mymod.py, which has three functions:

count_lines(name) function that reads an input file and counts the number of lines in it (hint: file.readlines() 
does most of the work for you, and len does the rest) 
count_chars(name) function that reads an input file and counts the number of characters in it (hint: file.read() 
returns a single string)
test(name) function that calls both counting functions with a given input file­name. Such a filename generally 
might be passed-in, hard-coded, input with raw_input, or pulled from a command-line via the sys.argv list; 
for now, assume it's a passed-in function argument.


All three mymod.py functions should expect a filename string to be passed in. 

Test your module interactively, using import and name qualification to fetch your exports. 

Does your PYTHONPATH need to include the directory where you created mymod.py?
"""
from mymod import count_lines, count_chars, test

file_name =  r'C:\Users\forte\Desktop\Beetroot_course\Tasks\Modules_directory\sample.txt'

print(test(file_name))
