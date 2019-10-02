class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def addNode(self, node):
        if node.value < self.value and node.value != self.value:
            if self.left == None:
                self.left = node
            else:
                self.left.addNode(node)
        elif node.value > self.value and node.value != self.value:
            if self.right == None:
                self.right = node
            else:
                self.right.addNode(node)

    def search(self, val):
        if val == self.value:
            return "Found"

        elif val < self.value:
            if self.left != None:
                return self.left.search(val)
            else:
                return "Not Found "
        elif val > self.value:
            if self.right != None:
                return self.right.search(val)
            else:
                return "Not Found"

    def traverse(self):
        _list = []
        if self.left.value != None:
            self.left.traverse()
        _list.append(self.value)
        self.right.traverse()
        return _list


class BinaryTree:
    def __init__(self):
        self.root = None

    def addVlaue(self, val):
        node = Node(val)
        if self.root == None:
            self.root = node
        else:
            self.root.addNode(node)

    def search(self, val):
        if self.root == None:
            return False
        else:
            return self.root.search(val)

    # def travelsel(self):
    #     if self.root == None:
    #         return []
    #     return self.root.traverse()


import random

tree = BinaryTree()
for i in range(10):
    t = random.randint(0, 100)
    tree.addVlaue(t)
    print(t)
print(tree.search(3))
print(tree.travelsel())
