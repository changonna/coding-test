from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    # 0. min_dis
    MAX = 10000001
    min_dis = [MAX for _ in range(n + 1)]
    answer = [0, MAX]

    set_summits = set(summits)
    
    # 1. paths -> graph
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    # 2. dijkstra
    pq = [(0, gate) for gate in gates] # (cost, node)
    
    # [[0,1], [0,3]]
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)

        if cur_cost >= min_dis[cur_v]:
            continue
        min_dis[cur_v] = cur_cost

        for next_cost, next_v in graph[cur_v]:
            # (3, 2) / (4, 4) (5, 2)
            # (4, 5) (2, 4) (5, 3) (3, 1) / (2, 2), (4, 3) (3, 5) (1, 6)
            total_cost = max(cur_cost, next_cost)
            if total_cost >= min_dis[next_v]:
                continue
            # # heappush 전에 산봉우리 노드 만나면 continue
            if cur_v in set_summits: # 탐색시 시간복잡도 줄이기 list=O(n) -> set=O(1)
                continue
            # min_dis[next_v] = next_cost
            heapq.heappush(pq, (total_cost, next_v))
    
    for summit in summits:
        if answer[1] > min_dis[summit]:
            answer = [summit, min_dis[summit]]
        # intensity가 같으면 산봉우리 번호가 작은 값 선택
        elif answer[1] == min_dis[summit] and summit < answer[0]:
            answer[0] = summit
    return answer

# [MAX, 0, 3, 0, 3, 3, 3]
# [5, 3]


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
res = solution(n, paths, gates, summits)
print(res)