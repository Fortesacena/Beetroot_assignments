#---------------------------TASK 1-----------------------------
"""Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. 
Make another method called talk() which makes prints a greeting from the person containing, for example like this:

"Hello, my name is Carl Johnson and I'm 26 years old"""

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def talk(self):
        print (f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")

obj = Person("Carl", "Johnson", 20)
obj.talk()

#---------------------------TASK 2-----------------------------
"""Task 2

Doggy age

Create a class Dog with class attribute age_factor equals to 7. Make __init__() 
which takes values for a dog's age. Then create a method human_age which returns 
the dog's age in human equivalent."""

class Dog:
    age_factor = 7
    def __init__(self, dog_age):
        self.dog_age=dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor


dog1 = Dog(3)
print(f"The dog's age in human equivalent is: {dog1.human_age()} years")

dog2 = Dog(5)
print(f"The dog's age in human equivalent is: {dog2.human_age()} years")

#---------------------------TASK 3-----------------------------
"""Task 3

TV controller

Create a simple prototype of a TV controller in Python. It'll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

The default channel turned on before all commands is №1."""

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[len(self.channels) - 1]

    def turn_channel(self, channel_number):
        if 1 <= channel_number <= len(self.channels):
            return self.channels[channel_number - 1]

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, identifier):
        if isinstance(identifier, int) and 1 <= identifier <= len(self.channels):
            return "Yes"
        elif isinstance(identifier, str) and identifier in self.channels:
            return "Yes"
        else:
            return "No"


channels_list = ["BBC","Discovery", "TV1000"]

controller = TVController(channels_list)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"