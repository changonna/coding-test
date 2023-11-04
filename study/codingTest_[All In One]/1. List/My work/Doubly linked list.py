'''
Linked List를 직접 구현해보자
''' 

class Node :
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList(object):
    def __init__(self):
        # 초기 head, tail은 None 설정
        self.head = None
        self.tail = None
    def insert_back(self, value):
        new_node = Node(value) # 노드 생성
        # 첫 node 생성시에만 실행
        if self.head is None:
            # head, tail이 첫번째 노드를 가리키도록 설정
            self.head = new_node
            self.tail = new_node
        else: # 맨 뒤의 node가 new_node를 가리켜야 한다.
            # O(1)로 insert_back
            self.tail.next = new_node # 마지막노드인 tail의 next를 새로운 노드를 가리키게 하고
            new_node.prev = self.tail # 새 노드의 prev를 이전 tail로
            self.tail = self.tail.next # tail을 tail의 next(추가된 노드)를 가리키도록
    def remove_back(self):
        self.tail = self.tail.prev
        self.tail.next = None
    def insert(self, idx, value):
        new_node = Node(value)
        if(idx == 0):
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node    
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            next_node = current.next
            current.next = new_node
            new_node.prev = current
            next_node.prev = new_node
            new_node.next = next_node
    def remove(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        if(idx == 0):
            self.head = current.next
            current.next.prev = None
            current.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
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

ll.remove_back()
ll.print() # 1->2->3

ll.insert(1, 10)
ll.print() # 1->10->2->3

ll.insert(3, 30)
ll.print() # 1->10->2->30->3

ll.insert(0, 0)
ll.print() # 0->1->10->2->30->3

print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))
print(ll.get(4))
print(ll.get(5))

ll.remove(2)
ll.print() # 0->1->2->30->3

ll.remove(1)
ll.print() # 0->2->30->3

ll.remove(0)
ll.print() # 2->30->3

print(ll.get(0))
print(ll.get(1))
print(ll.get(2))