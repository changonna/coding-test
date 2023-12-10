import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]

heapq.heapify(min_heap)
heapq.heappop(min_heap)
heapq.heappush(min_heap, 1)

print(min_heap)