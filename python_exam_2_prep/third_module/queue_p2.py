# queue_p2.py

class QueueError(IndexError):
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
    
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        if not self._Queue__queue_list:
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")