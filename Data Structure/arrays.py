#Array 1 dimensi implementasi OOP

from arrays import Array

class Array(object):
    def __init__(self, capacity, fillValue=None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __setitem__(self, index, newItem):
        self.items[index] = newItem

    def __getitem__(self, index):
        return self.items[index]
    

        
# Create an instance of the Array class with a capacity of 5
array_instance = Array(5)

# Populate the array with values
for i in range(len(array_instance)):
    array_instance[i] = i + 1

# The array is now populated, and no print statements are included.
for item in array_instance:
    pass  # Iterate through the array without printing
