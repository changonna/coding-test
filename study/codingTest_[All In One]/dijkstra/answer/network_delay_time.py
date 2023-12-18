from collections import defaultdict
import heapq

class Solution(object):
  def networkDelayTime(self, times, n, k):
    # 1. 그래프 구현
    graph = defaultdict(list) # dictionary의 원소의 기본형은 list다
    for u, v, w in times:
      graph[u].append((w, v))

    # 2. dijkstra algorithm
    costs = {}
    pq = []
    heapq.heappush(pq, (0, k))

    while pq:
      cur_cost, cur_v = heapq.heappop(pq)
      if cur_v not in costs:
        costs[cur_v] = cur_cost
        for next_cost, next_v in graph[cur_v]:
          total_cost = next_cost + cur_cost
          heapq.heappush(pq, (total_cost, next_v))
    # 3. 방문 못한 노드 찾기
    for i in range(1, n+1):
      if i not in costs:
        return -1
    # 4. 최소값중에서 최대값 구하기
    return max(costs.values())
  

  
times = [[2,1,2], [2,3,5], [2,4,1], [4,3,3]]
res = Solution().networkDelayTime(times, 4, 2)
print(res) # 4

times = [[2,1,1],[2,3,1],[3,4,1]]
res = Solution().networkDelayTime(times, 4, 2)
print(res) # 2

times = [[1,2,1]]
res = Solution().networkDelayTime(times, 2, 1)
print(res) # 1

times = [[1,2,1]]
res = Solution().networkDelayTime(times, 2, 2)
print(res) # -1
