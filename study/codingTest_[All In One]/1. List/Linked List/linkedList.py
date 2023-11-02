'''
Linked List를 직접 구현해보자
''' 

class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
first.value = 6







class LinkedList(object):
    def __init__(self):
        self.head = None # 초기 head는 None
    def append(self, value):
        new_node = Node(value) # 노드 생성
        # 첫 node 생성시에만 실행
        if self.head is None:
            self.head = new_node # head가 첫번째 노드를 가르켜야 한다.
        else: # 맨 뒤의 node가 new_node를 가리켜야 한다.
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node # 마지막이었던 노드가 새로 추가된 노드를 가리키도록
    def get(self, idx):
        pass
    def insert(self, idx, value):
        pass
    def delete(self, idx):
        pass

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)