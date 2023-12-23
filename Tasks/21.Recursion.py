#############################################
# All tasks should be solved using recursion
#############################################

#---------------------Task1-----------------------------

# from typing import Optional
# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
#     """
#     Returns  x ^ exp

#     >>> to_power(2, 3) == 8
#     True

#     >>> to_power(3.5, 2) == 12.25
#     True

#     >>> to_power(2, -1)
#     ValueError: This function works only with exp > 0.
#     """
#     pass

from typing import Optional


def to_power(x: float, exp: float) ->float:
    if exp < 0:
        raise ValueError ("This function works only with exp > 0")
    elif exp == 0:
        return 1
    else:
        return x * to_power(x, exp - 1)


assert to_power(2, 3) == 8
assert to_power(3.5, 2)==12.25
# to_power(2, -1)


#--------------------------------Task2--------------------
# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     """
#     Checks if input string is Palindrome
#     >>> is_palindrome('mom')
#     True

#     >>> is_palindrome('sassas')
#     True

#     >>> is_palindrome('o')
#     True
#     """
#     pass

from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if (looking_str == looking_str[::-1]):
        return True
    else:
        return False
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    pass

assert is_palindrome('mom')
assert is_palindrome('sassas')
assert is_palindrome('o')


#-----------------------------------Task3-------------------------------
# from typing import Optional
# def mult(a: int, n: int) -> int:
#     """
#     This function works only with positive integers

#     >>> mult(2, 4) == 8
#     True

#     >>> mult(2, 0) == 0
#     True

#     >>> mult(2, -4)
#     ValueError("This function works only with postive integers")
#     """

def mult(a: int, n: int) -> int:
    if a<0 or n<0:
        raise ValueError("This function works only with positive integers")
    else:
        return a * n
    
assert mult(2, 4) == 8
assert mult(2, 0) == 0

#--------------------------------Task4-----------------------
# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     >>> reverse("hello") == "olleh"
#     True
#     >>> reverse("o") == "o"
#     True
#     """

def reverse(input_str: str) -> str:
    return input_str[::-1]

assert reverse("hello") == "olleh"
assert reverse("o") == "o"


#---------------------------------Task5-----------------------
# def sum_of_digits(digit_string: str) -> int:
#     """
#     >>> sum_of_digits('26') == 8
#     True

#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")
#     """

#------------------Version without using recursion
# def sum_of_digits(input_value) -> int:
#     digit_string = str(input_value)
    
#     for digit in digit_string:
#         if not digit.isdigit():
#             raise ValueError("Input must be an integer or a digit string")

#     return sum(int(digit) for digit in digit_string)

# assert  sum_of_digits('26') == 8

#with recursion
def sum_of_digits(input_value) -> int:
    digit_string = str(input_value)
    
    def is_digit(char):
        return '0' <= char <= '9'

    def helper(index):
        if index == len(digit_string):
            return 0
        elif not is_digit(digit_string[index]):
            raise ValueError("Input must be an integer or a digit string")
        else:
            return int(digit_string[index]) + helper(index + 1)

    return helper(0)

assert  sum_of_digits('26') == 8

