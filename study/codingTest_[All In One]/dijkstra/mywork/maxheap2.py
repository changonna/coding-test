# min heap을 만드는 것 같지만
# -1을 곱해서 max Heap을 만든다.

import heapq

max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap] # [-5, -3, -9, -4, -1, -2, -6]
heapq.heapify(max_heap) # [-9, -4, -6, -3, -1, -2, -5]
weight = heapq.heappop(max_heap) # -9
value = -1 * weight # 9

print(value) # 9