import heapq
class Solution(object):
  def networkDelayTime(self, times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    costs = {}
    pq = []
    # 1. 그래프 구현 : times를 graph로 변경
    graph = { i:[] for i in range(1, n+1) }

    # 2. 다익스트라 알고리즘
    for cur_v, next_v, cur_cost in times:
      graph[cur_v].append((cur_cost, next_v))

    heapq.heappush(pq, (0, k))

    while pq:
      cur_cost, cur_v = heapq.heappop(pq)

      if cur_v not in costs:
        costs[cur_v] = cur_cost

        for next_cost, next_v in graph[cur_v]:
          total_cost = cur_cost + next_cost
          heapq.heappush(pq, (total_cost, next_v))

    # 3. 방문 못한 노드 찾기 : costs와 n의 길이가 같으면 모두 갈 수 있으니까
    if len(costs) == n:
      # 4. 최소값중에서 최대값 구하기
      return max(costs.values())
    return -1





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
