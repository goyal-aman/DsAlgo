class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def top(self):
        return self.tail.next.data 
    
    def bottom(self):
        return self.tail.data


    def enqueue(self, data):
        new_node = node(data, None)
        if self.is_empty():
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size+=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("EmptyQueue")
        ans = self.tail.next.data
        self.tail.next = self.tail.next.next

mylist = CircularQueue()
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
print(mylist.top())
