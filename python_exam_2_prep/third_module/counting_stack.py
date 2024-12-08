# counting_stack.py

# Scenario
# We've showed you recently how to extend Stack
# possibilities by defining a new class (i.e., a
# subclass) which retains all inherited traits
# and adds some new ones.

# Your task is to extend the Stack class behavior
# in such a way so that the class is able to
# count all the elements that are pushed and
# popped (we assume that counting pops is
# enough).

# Run it to check whether your code outputs 100.

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


# Define a counting subclass by pointing to the
# Stack superclass.
class CountingStack(Stack):
    # Define CountingStack constructor
    def __init__(self):
        # Invoke the superclass's constructor
        # explicitly
        Stack.__init__(self)
        # introduce a property designed to count
        # pop operations and name it in a way
        # which guarantees hiding it;
        # initialize it to zero inside the
        # constructor
        self.__counter = 0

    # provide a method which returns the value
    # currently assigned to the counter
    # (name it get_counter()).
    def get_counter(self):
        return self.__counter

    def pop(self):
        Stack.pop(self)
        self.__counter += 1

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())