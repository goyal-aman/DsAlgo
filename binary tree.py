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

    def traverse(self, tree_elements=None):
        if tree_elements is None:
            tree_elements = []
        if self.left != None:
            self.left.traverse(tree_elements=tree_elements)
        tree_elements.append(self.value)
        if self.right != None:
            self.right.traverse(tree_elements=tree_elements)
        return tree_elements


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

    def traverse(self):
        if self.root == None:
            return "no data"
        else:
            return self.root.traverse()


if __name__ == "__main__":

    import random

    tree = BinaryTree()
    elements = []
    for i in range(10):
        j = random.randint(0, 100)
        elements.append(j)
        tree.addVlaue(j)

    print(f"elements: {elements}")
    print(f"sorted elements: {sorted(elements)}")

    print("output from tree: ")
    print("\n", tree.traverse())
