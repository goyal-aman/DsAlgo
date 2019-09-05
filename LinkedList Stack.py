'''
Implementation of Stack using LinkedList
'''
class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return len.size == 0
    
    def push(self, data):
        self.head = node(data, self.head)
        self.size += 1
    
    def top(self):
        '''
        returns the top element of the step
        without deleting it.
        '''
        if self.size == 0:
            raise Exception('Empty Stack')
        else:
            return self.head.data
    
    def pop(self):
        if self.size <= 0:
            raise Exception('Empty Stack')
        ans = self.head.data
        self.head = self.head.next
        self.size -= 1
        return ans
mylist = LinkedListStack()
mylist.push(1)
mylist.push(2)