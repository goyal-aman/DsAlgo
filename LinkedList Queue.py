class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size <= 0
    
    def top(self):
        '''
        return top/first element from the stack
        '''
        return self.head.data

    def enqueue(self,data):
        new_node = node(data, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size +=1
    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty queue')
        ans = self.head.data
        self.head = self.head.next
        self.size-=1
        return ans


mylist = LinkedListQueue()
print(len(mylist))
print(mylist.is_empty())
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
mylist.dequeue()
mylist.dequeue()
mylist.dequeue()
mylist.enqueue(1)
mylist.enqueue(2)