# stack_object_approach.py

# Define the Stack class.
class Stack:
    # Define the constructor function.
    def __init__(self):
        # Add a list property
        # Use encapsulation '__' to make property
        # private to the class
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# Instantiate the object.
stack_object = Stack()

# Access properties using dot notation
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())