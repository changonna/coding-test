'''
Doubly linked list

tail 있고
prev 있고 next 있고
'''

class Node :
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def remove_back(self):
        pass
    def insert(self, idx, value):
        pass
    def remove(self, idx):
        pass
    def print(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print('->', end='')


ll = LinkedList()
ll.insert_back(1)
ll.insert_back(2)
ll.insert_back(3)
ll.insert_back(4)
ll.print()

