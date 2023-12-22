#---------------------------TASK 1-----------------------------
"""Not your boring middle school homework — these tasks will help you in real life! Have fun with your assignment for this topic:

Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

"add called with 4, 5"


def logger(func):
    pass


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]"""


def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(f"{key}={repr(value)}" for key, value in kwargs.items())

        print(f"{func.__name__} called with {args_str}, {kwargs_str}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(1, 2, 3)

#---------------------------TASK 2-----------------------------

"""Write a decorator that takes a list of stop words and replaces them with * 
inside the decorated function"""

def stop_words(words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result

        return wrapper

    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# Test the decorated function
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

#---------------------------TASK 3-----------------------------
"""Task 3

Write a decorator arg_rules() that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
"""

def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                # Check type
                if not isinstance(arg, type_):
                    print(f"Validation failed: Argument type should be {type_}")
                    return False

                # Check max length
                if isinstance(arg, str) and len(arg) > max_length:
                    print(f"Validation failed: Argument length should be at most {max_length}")
                    return False

                # Check contains
                if any(symbol not in arg for symbol in contains):
                    print(f"Validation failed: Argument should contain symbols {contains}")
                    return False

            return func(*args, **kwargs)

        return wrapper

    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
