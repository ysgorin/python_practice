# queue_p1.py

# Scenario
# As you already know, a stack is a data
# structure realizing the LIFO (Last In – First
# Out) model. It's easy and you've already grown
# perfectly accustomed to it.

# Let's try something new now. A queue is a data
# model characterized by the term FIFO: First In
# – First Out. Note: a regular queue (line) you
# know from shops or post offices works exactly
# in the same way – a customer who came first is
# served first too.

# Your task is to implement the Queue class with
# two basic operations:

# put(element), which puts an element at end of
# the queue;

# get(), which takes an element from the front of
# the queue and returns it as the result (the
# queue cannot be empty to successfully perform
# it.)

# Expected output
# 1
# dog
# False
# Queue error

class QueueError(IndexError): # Choose base class for the new exception.
    # No need to explicitly invoke the Exception
    # constructor unless adding custom attributes
    # or behavior to the exception. 
    pass

class Queue:
    def __init__(self):
        # use a list as your storage
        self.__queue_list = []

    def put(self, elem):
        # put() should append elements to the
        # beginning of the list
        self.__queue_list.insert(0,elem)

    def get(self):
        # get() should remove the elements from
        # the end of the list
        if not self.__queue_list:
            raise QueueError
        return self.__queue_list.pop()

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")