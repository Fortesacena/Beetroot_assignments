#---------------------------TASK 1-----------------------------

"""Pick your solution to one of the exercises in this module. Design tests for this solution and write 
tests using unittest library. """


import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbersFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add_numbers(2, -3)
        self.assertEqual(result, -1)

    def test_add_float_numbers(self):
        result = add_numbers(2.5, 3.5)
        self.assertEqual(result, 6.0)

if __name__ == '__main__':
    unittest.main()


#---------------------------TASK 2-----------------------------
"""Write tests for the Phonebook application, which you have implemented in module 1. Design tests 
for this solution and write tests using unittest library"""


class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def get_contact(self, name):
        return self.contacts.get(name)

    def delete_contact(self, name):
        del self.contacts[name]

    def clear(self):
        self.contacts.clear()

import unittest

class TestPhonebookApplication(unittest.TestCase):
    def setUp(self):
       
        self.phonebook = Phonebook()
        self.phonebook.add_contact("John Doe", "123456789")
        self.phonebook.add_contact("Jane Doe", "987654321")

    def tearDown(self):
        
        self.phonebook.clear()

    def test_add_contact(self):
        self.phonebook.add_contact("Alice", "111222333")
        self.assertEqual(self.phonebook.get_contact("Alice"), "111222333")

    def test_get_contact(self):
        result = self.phonebook.get_contact("John Doe")
        self.assertEqual(result, "123456789")

    def test_get_nonexistent_contact(self):
        with self.assertRaises(KeyError):
            self.phonebook.get_contact("Nonexistent")

    def test_delete_contact(self):
        self.phonebook.delete_contact("Jane Doe")
        with self.assertRaises(KeyError):
            self.phonebook.get_contact("Jane Doe")

if __name__ == '__main__':
    unittest.main()
