import heapq

max_heap = [5, 3, 9, 4, 1, 2, 6]
heapq._heapify_max(max_heap)
value = heapq._heappop_max(max_heap)

print(max_heap) # [6, 4, 5, 3, 1, 2]