'''
Linked List를 직접 구현해보자
''' 

class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
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
            self.tail = self.tail.next # tail을 tail의 next(추가된 노드)를 가리키도록
    def get(self, idx):
        current = self.head
        for _ in range(idx): # idx만큼 이동
            current = current.next
        return current.value # value 반환
    def insert(self, idx, value): # O(n)
        new_node = Node(value)
        if(idx == 0):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next # current는 추가할 노드의 이전 노드를 가리킨다
            new_node.next = current.next # 새 노드의 next는 current의 next
            current.next = new_node # current의 next는 새 노드
    def delete(self, idx):
        before_node = self.get(idx - 1)
        after_node = self.get(idx + 1)
        before_node.next = after_node



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
# ll.get(0)
# ll.get(1)
# ll.get(3)

print(ll.get(2).value)

ll.insert(2, 10)
print(ll.get(2).value)

ll.delete(2)
print(ll.get(2).value)
