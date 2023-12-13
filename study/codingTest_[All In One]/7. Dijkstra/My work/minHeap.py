import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]

heapq.heapify(min_heap) # [1, 3, 2, 4, 5, 9, 6]
heapq.heappop(min_heap) # [2, 3, 6, 4, 5, 9]
heapq.heappush(min_heap, 1) # [1, 3, 2, 4, 5, 9, 6]

print(min_heap) # [1, 3, 2, 4, 5, 9, 6]