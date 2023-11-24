#---------------------------TASK 1-----------------------------

"""File Context Manager class

Create your own class, which can behave like a built-in function open(). Also, you need to extend its 
functionality with counter and logging. Pay special attention to the implementation of __exit__ method, 
which has to cover all the requirements to context managers"""

import logging

class File_Context_Manager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.operation_count = 0


    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.operation_count = 0
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            logging.info(f"File '{self.filename}' closed.")
        logging.info(f"Total operations on file: {self.operation_count}")

filename = "example.txt"
mode = "w"

with File_Context_Manager(filename, mode) as file:
    file.write("Hello, this is a test.")
    
#---------------------------TASK 2-----------------------------

import unittest
import os

class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        
        self.filename = "test_file.txt"
        with open(self.filename, "w") as test_file:
            test_file.write("Initial content")

    def test_successful_read(self):
        with File_Context_Manager(self.filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "Initial content")

    def test_successful_write(self):
        with File_Context_Manager(self.filename, "a") as file:
            bytes_written = file.write("\nAdditional content")
            self.assertEqual(bytes_written, len("\nAdditional content"))

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            with File_Context_Manager("nonexistent_file.txt", "r") as file:
                pass

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            with File_Context_Manager(self.filename, "invalid_mode") as file:
                pass

    def test_read_after_close(self):
        with File_Context_Manager(self.filename, "r") as file:
            pass
        with self.assertRaises(ValueError):
            file.read()

    def test_write_after_close(self):
        with File_Context_Manager(self.filename, "a") as file:
            pass
        with self.assertRaises(ValueError):
            file.write("Attempt to write after close")

if __name__ == '__main__':
    unittest.main()

