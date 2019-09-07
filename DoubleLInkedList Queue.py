class node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

class doubleLinkedList:
    def __init__(self):
        self.head = node(None, None, None)
        self.trailer = node(None, None, None)
        self.head.next = self.trailer
        self.trailer.prev = self.head
        self.size = 0 


    def __len__(self):
        return self.size 
    
    
    def is_empty(self):
        return self.size == 0
    
    def insert_between(self, data, predecessor, successor):
        new_node = node(data, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node.data
    
    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        data = node.data
        predecessor = successor = node.data = None
        self.size -= 1
        return data
    
class DoubleLinkeddequeue(doubleLinkedList):
    def first(self):
        return self.head.next.data

    def last(self):
        return self.trailer.prev.data
    
    def push_first(self, data):
        self.insert_between(data, self.head ,self.head.next)
    def push_last(self, data):
        self.insert_between(data, self.trailer.prev, self.trailer)
    def pop_first(self):
        return self.delete_node(self.head.next)
    def pop_last(self):
        return self.delete_node(self.trailer.prev)

mylist = DoubleLinkeddequeue()
mylist.push_first(3)
mylist.push_first(2)
mylist.push_first(1)
mylist.pop_first()
mylist.pop_first()
print(mylist.first())

mylist.push_last(4)
mylist.push_last(5)
mylist.push_last(6)
mylist.pop_last()
print(mylist.last())