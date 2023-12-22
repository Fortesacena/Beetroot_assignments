#---------------------------TASK 1-----------------------------

"""
Create a class method named validate, which should be called from the __init__ 
method to validate parameter email, passed to the constructor. The logic inside 
the validate method could be to check if the passed email parameter is a valid 
email string."""

import re

class MyClass:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    def validate(self, email):
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if not email_pattern.match(email):
            raise ValueError("Invalid email format")
        
try:
    obj = MyClass("test@example.com")
    print(f"Email validation successful. Email: {obj.email}")
except ValueError as e:
    print(f"Error: {e}")

#---------------------------TASK 2-----------------------------
"""Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property boss, and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his 
own workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to 
add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

"""
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self._id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def id(self):
        return self._id

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker can be added as workers.")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self._id = id_
        self.name = name
        self.company = company
        self._boss = None  
        self.boss = boss 

    @property
    def id(self):
        return self._id

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if new_boss is None or isinstance(new_boss, Boss):
            if self._boss:
                self._boss.workers.remove(self)
            self._boss = new_boss
            if new_boss:
                new_boss.add_worker(self)
        else:
            raise ValueError("The boss must be either None or an instance of Boss.")



boss1 = Boss(id_=1, name="Boss 1", company="ABC Corp")
boss2 = Boss(id_=2, name="Boss 2", company="XYZ Inc")

worker1 = Worker(id_=101, name="Worker 1", company="ABC Corp", boss=boss1)
worker2 = Worker(id_=102, name="Worker 2", company="ABC Corp", boss=boss1)

print("Boss 1's workers:", [worker.id for worker in boss1.workers])
print("Boss 2's workers:", [worker.id for worker in boss2.workers])

worker1.boss = boss2

print("Boss 1's workers:", [worker.id for worker in boss1.workers])
print("Boss 2's workers:", [worker.id for worker in boss2.workers])


#---------------------------TASK 3-----------------------------
"""Write a class TypeDecorators which has several methods for converting results of functions to a specified 
type (if it's possible):

methods:

to_int

to_str

to_bool

to_float


Don't forget to use @wraps"""

from functools import wraps

class TypeDecorators:
    @classmethod
    def to_int(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)
        return wrapper
    
    @classmethod
    def to_str(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper
    
    @classmethod
    def to_bool(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper
    
    @classmethod
    def to_float(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)
        return wrapper
    

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True