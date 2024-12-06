# stack_object_approach.py

# Define the Stack class.
class Stack:
    # Define the constructor function.
    def __init__(self):
        # Add a list property
        self.stack_list = []

# Instantiate the object.
stack_object = Stack()
# Access property using dot notation
print(len(stack_object.stack_list))