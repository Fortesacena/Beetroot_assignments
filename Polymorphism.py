#---------------------------TASK 1-----------------------------
"""Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: 
Dog and Cat, and make their own implementation of the method talk be different. For instance, 
Dog's can be to print "woof woof", while Cat's can be to print "meow".

Also, create a simple generic function, which takes as input instance of a Cat or Dog 
classes and performs talk method on input parameter.  """

class Animal:
    def talk():
        pass

class Dog(Animal):
    def talk(self):
        print("Woof")

class Cat(Animal):
    def talk(self):
        print("Meow")

def make_animal_talk(animal):
    animal.talk()


dog_instance = Dog()
cat_instance = Cat()

dog_instance.talk()
cat_instance.talk()

print(make_animal_talk(dog_instance))
print(make_animal_talk(cat_instance))


#---------------------------TASK 2-----------------------------

"""Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.


Also, the book class should have a class variable which holds the amount of all existing books"""

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"{self.name} ({self.birthday}), {self.country}"

class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"{self.name} ({self.year}), by {self.author.name}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"{self.name} Library"
    
author1 = Author("Author1", "Country1", "2000-01-01")
author2 = Author("Author2", "Country2", "1990-02-02")

library = Library("City Library")

book1 = library.new_book("Book1", 2005, author1)
book2 = library.new_book("Book2", 2010, author2)
book3 = library.new_book("Book3", 2005, author1)

books_by_author = library.group_by_author(author1)
books_by_year = library.group_by_year(2005)

print(f"Total books in the library: {Book.total_books}")
print(f"{library} contains:")
for book in library.books:
    print(f"  - {book}")

print(f"\nBooks by {author1.name}:")
for book in books_by_author:
    print(f"  - {book}")

print(f"\nBooks from the year 2005:")
for book in books_by_year:
    print(f"  - {book}")


#---------------------------TASK 3-----------------------------
"""Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) 
with appropriate checking and error handling
"""

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Both numerator and denominator must be integers")

        common = gcd(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type. Must be Fraction.")
        
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type. Must be Fraction.")
        
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type. Must be Fraction.")
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type. Must be Fraction.")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

sum_fraction = fraction1 + fraction2
difference_fraction = fraction1 - fraction2
product_fraction = fraction1 * fraction2
quotient_fraction = fraction1 / fraction2

print(f"Fraction 1: {fraction1}")
print(f"Fraction 2: {fraction2}")
print(f"Sum: {sum_fraction}")
print(f"Difference: {difference_fraction}")
print(f"Product: {product_fraction}")
print(f"Quotient: {quotient_fraction}")
