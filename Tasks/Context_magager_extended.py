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
    
