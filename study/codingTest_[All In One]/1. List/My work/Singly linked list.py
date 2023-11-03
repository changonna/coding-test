'''
Singly linked list

tail 없고, prev 없고
next 있고
current 사용
'''

class Node():
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
    # O(n)
    def insert_back(self, value):
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    # O(n)
    def insert(self, idx, value):
        new_node = Node(value)
        current = self.head
        if(idx == 0):
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(idx-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    # O(n)
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    # O(n)
    def remove(self, idx):
        current = self.head
        if(idx == 0):
            self.head = current.next
            current.next = None ## 이 부분은 안해도 되는듯?
        else:
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next
    def print(self):
        current = self.head
        while(current):
            print(current.value, end="")
            current = current.next
            if(current):
                print('->', end="")
        print()

ll = LinkedList()
ll.insert_back(1)
ll.insert_back(2)
ll.insert_back(3)
ll.insert_back(4)
ll.print() # 1->2->3->4

ll.insert(2, 10)
ll.print() # 1->2->10->3->4

print(ll.get(0)) # 1
print(ll.get(1)) # 2
print(ll.get(2)) # 10
print(ll.get(3)) # 3
print(ll.get(4)) # 4

ll.remove(0) 
ll.print() # 2->10->3->4
ll.remove(1)
ll.print() # 2->3->4