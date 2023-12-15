'''
Queue : 선입선출 FIFO(First In First Out)
Linked List 기반 구현

[ deque 메소드 ]
- append() : 오른쪽 값 추가
- appendleft() : 왼쪽 값 추가

- pop() : 오른쪽 값 제거
- popleft() : 왼쪽 값 제거
'''

# deque imprt
from collections import deque

# deque 생성
q = deque()

'''

'''

# enqueue - 시간복잡도 O(1)
q.append(1) # [1]
q.append(2) # [1, 2]
q.appendleft(0) # [0, 1, 2]

# dequeue - 시간복잡도 O(1)
q.pop() # [0, 1]
q.popleft() # [1]

print(q)