
#---------------------------TASK 1-----------------------------
"""Write a function called oops that explicitly raises an IndexError exception 
when called. Then write another function that calls oops inside a try/except 
state­ment to catch the error. What happens if you change oops to raise KeyError 
instead of IndexError?"""

def oops():
    raise IndexError("The number of the index is out of range!")

def funct():
    list = [1,2,3,4,5,6,7]
    x= int(input("Input the number of any index of the list:"))
    try:
        if x>len(list):
            oops()
        else:
            print(list[x])
    except IndexError as e:
        print(f'Error: {e}')

funct()

#---------------------------TASK 2-----------------------------
"""Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided 
by b, construct a try-except block which raises an exception if the two 
values given by the input function were not numbers, and if value b was 
zero (cannot divide by zero)."""

def task_2():
    try:
        a=int(input("Input the value of a:"))
        b=int(input("Input the value of b:"))

        result = a**2 - b
        print("The result of squared a divided by b is: ", result)
    except ValueError as e:
        print(f'Error: {e}')
    
task_2()

