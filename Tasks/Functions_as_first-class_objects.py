#---------------------------TASK 1-----------------------------
"""
Write a Python program to detect the number of local variables declared in a function.
"""

def my_function():
    variable1 = 10
    variable2 = "Hello"
    variable3 = [1, 2, 3]
    variable4 = {'a': 1, 'b': 2}
    
    local_vars = locals()
    count = len(local_vars)
    
    return count


num_of_locals = my_function()
print(f"The number of local variables in 'my_function' is: {num_of_locals}")


#---------------------------TASK 2-----------------------------
"""
Write a Python program to access a function inside a function (Tips: use function, which 
returns another function)
"""

def greetings(greeting_type):
    if greeting_type == "informal":
        def informal_greeting(name):
            return f"Hey {name}! What's up?"
        
        return informal_greeting

    elif greeting_type == "formal":
        def formal_greeting(name):
            return f'Good morning, {name}. How do you do?'
        return formal_greeting
    
    else:
        def default_greeting(name):
            return f"Hello, {name}. Nice to meet you."
        return default_greeting
    
informal = greetings("informal")
formal = greetings("formal")
default = greetings("default")

print(informal('Filan'))
print(formal('Fistek'))
print(default('Filan Fisteku'))

#---------------------------TASK 3-----------------------------
"""
Write a function called choose_func() which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return 
the result of it. Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2):
"""

def choose_func(nums: list, func1, func2):
    if all(val>0 for val in nums):
        return func1(nums)
    
    else:
        return func2(nums)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
