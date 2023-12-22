#---------------------------TASK 1-----------------------------
"""Create your own implementation of a built-in function enumerate, named with_index(), 
which takes two parameters: iterable and start, default is 0. Tips: see the documentation 
for the enumerate function"""

def with_index(iterable, start=0):
    for i in range(start, len(iterable)+start):
        yield i, iterable[i-start]

my_list = ['apple', 'banana', 'orange']

for index, value in with_index(my_list, start=1):
    print(f"Index: {index}, Value: {value}")


#---------------------------TASK 2-----------------------------
"""Create your own implementation of a built-in function range(), named in_range(), which takes three 
parameters: start, end, and optional step. Tips: See the documentation for range() function"""

def in_range(start, end, step=1):
    current = start
    while(step>0 and current<end) or (step<0 and current>end):
        yield current
        current +=start

    
for i in in_range(1, 10, 2):
    print(i)

#---------------------------TASK 3-----------------------------

"""Create your own implementation of an iterable, which could be used inside for-in loop. Also, 
add logic for retrieving elements using square brackets syntax."""

class MyIterable:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        current = self.start
        while (self.step > 0 and current < self.end) or (self.step < 0 and current > self.end):
            yield current
            current += self.step

    def __getitem__(self, index):
        if self.step > 0:
            if self.start + index * self.step < self.end:
                return self.start + index * self.step
            else:
                raise IndexError("Index out of range")
        elif self.step < 0:
            if self.start + index * self.step > self.end:
                return self.start + index * self.step
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("Step cannot be zero")


my_iterable = MyIterable(1, 10, 2)


for item in my_iterable:
    print(item)

print(my_iterable[0])  
print(my_iterable[1])  
print(my_iterable[2])  
