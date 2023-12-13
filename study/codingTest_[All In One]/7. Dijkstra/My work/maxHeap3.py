import heapq

max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [(-1 * i, i) for i in max_heap] # [(-5, 5), (-3, 3), (-9, 9), (-4, 4), (-1, 1), (-2, 2), (-6, 6)]
heapq.heapify(max_heap) # [(-9, 9), (-4, 4), (-6, 6), (-3, 3), (-1, 1), (-2, 2), (-5, 5)]
weight, value = heapq.heappop(max_heap) # (-9, 9)

print(value) # 9