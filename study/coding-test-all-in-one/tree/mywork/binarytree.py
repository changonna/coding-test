class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = 0
        self.left_child = None
        self.right_child = None

class BianaryTree:
    def __init__(self):
        self.root = None

bt = BianaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)
bt.root.right.right = Node(value = 6)

