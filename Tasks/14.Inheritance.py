#---------------------------TASK 1-----------------------------
"""Make a class structure in python representing people at school. Make a base class called Person, 
a class called Student, and another one called Teacher. Try to find as many methods and attributes 
as you can which belong to different classes, and keep in mind which are common and which are not. 
For example, the name should be a Person attribute, while salary should only be available to the teacher. """

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Student(Person):
    def __init__(self, name, age, gender, student_id, grade):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.grade = grade

    def study(self):
        return f"{self.name} is studying."

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Student ID: {self.student_id}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, gender, employee_id, subject, salary):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Employee ID: {self.employee_id}, Subject: {self.subject}, Salary: {self.salary}"


student1 = Student("Alice", 16, "Female", "S12345", "10th")
teacher1 = Teacher("Mr. Smith", 35, "Male", "T98765", "Math", 50000)

print(student1.get_details())
print(teacher1.get_details())

print(student1.study())
print(teacher1.teach())

#---------------------------TASK 2-----------------------------
"""Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'"""

class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums):
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(dates):
        def is_leap_year(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return [date for date in dates if is_leap_year(date)]


nums = [7, 11, 5, 4]
# nums=[26, -11, -8, 13, -90]
# nums=[2001, 1884, 1995, 2003, 2020]
m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

#---------------------------TASK 3-----------------------------
"""Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can't perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement 
additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type='name') - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store."""

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        product_with_price_premium = Product(product.type, product.name, product.price * 1.3)
        self.products.append({'product': product_with_price_premium, 'amount': amount})

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product in self.products:
            if identifier_type == 'name' and product['product'].name == identifier:
                product['product'].price *= (100 - percent) / 100
            elif identifier_type == 'type' and product['product'].type == identifier:
                product['product'].price *= (100 - percent) / 100

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product['product'].name == product_name:
                if product['amount'] >= amount:
                    product['amount'] -= amount
                    self.income += amount * product['product'].price
                else:
                    raise ValueError(f"Not enough {product_name} in stock.")
                return
        raise ValueError(f"{product_name} not found in the store.")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product['product'].type, product['product'].name, product['amount']) for product in self.products]

    def get_product_info(self, product_name):
        for product in self.products:
            if product['product'].name == product_name:
                return product['product'].name, product['amount']
        raise ValueError(f"{product_name} not found in the store.")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

#---------------------------TASK 4-----------------------------
"""Custom exception

Create your custom exception named CustomException, you can inherit from base Exception class, but extend 
its functionality to log every error message to a file named logs.txt. Tips: Use __init__ method to extend 
functionality for saving messages to file"""

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_to_file(msg)

    def log_to_file(self, msg):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")

try:
    raise CustomException("This is a custom error message.")
except CustomException as e:
    print(f"Caught an exception: {e}")
