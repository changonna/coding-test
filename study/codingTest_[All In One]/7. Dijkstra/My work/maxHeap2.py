import heapq

max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight

print(value) # 9