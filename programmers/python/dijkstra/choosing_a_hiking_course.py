'''
2022 KAKAO TECH INTERNSHIP
Level : 3
문제 : 등산코스 정하기
알고리즘 : dijkstra
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118669
'''

'''
n : 지점수 (1 ~ n)
gates : 출입구 번호 배열
summits: 산봉우리 번호 담긴 정수배열

2 <= n <= 50,000 = 5 * 10^4
n-1 <= paths(간선) <= 200,000 ≈ 2^18(262,144)

cost 최대 10,000,000 : 1 ≤ w ≤ 10,000,000

양방향
intensity : 가장 긴 시간을 해당 등산코스의 intensity

출입구(1) -> 원래 출입구(1)

출입구 -> 산봉우리 1곳 -> 원래 출입구

intensity 최소의 등산코스
'''
from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []
    min_summit = summits[0]
    
    # 1. paths -> graph로 변경하기
    graph = defaultdict(list)
    for v1, v2, cost in paths:
        graph[v1].append((cost, v2))
        graph[v2].append((cost, v1))
    # return graph
    
    # 2. dijkstra
    # 우선순위 큐에 한 번에 gates를 다 넣는다
    pq = [(0, gate) for gate in gates] # (현재 경로의 intensity, 현재 지점)

    # 최대값으로 min_dis를 초기화
    MAX = 10000001 # 최대값
    min_dis = [MAX for _ in range(n + 1)]

    while pq:
        intensity, cur_node = heapq.heappop(pq)
        if min_dis[cur_node] <= intensity:
            continue
        min_dis[cur_node] = intensity

        for next_cost, next_node in graph[cur_node]:
            next_cost = max(intensity, next_cost)
            if min_dis[next_node] <= next_cost:
                continue
            heapq.heappush(pq, (next_cost, next_node))

    return min_dis # [MAX, 0, 3, 0, 3, 3, 3]











    # # 2. dijkstra 함수 
    # # 시간복잡도 : O(E log E) = O(200,000 log 200,000) # 2^18 = 262,144
    # # = O(200,000 * 18) = 3.6 * 10^6 <= 10^7
    # def dijkstra(gate):
    #     costs = {}
    #     pq = []
    #     heapq.heappush(pq, (0, gate))

    #     while pq:
    #         cur_cost, cur_node = heapq.heappop(pq)
    #         if cur_node not in costs:
    #             costs[cur_node] = cur_cost
    #             for cost, next_node in graph[cur_node]:
    #                 next_cost = cur_cost + cost
    #                 heapq.heappush(pq, (next_cost, next_node))
    #     del costs[gate] # 본인 cost 삭제
    #     return costs
    # # return dijkstra(1)
    # # {"1":0,"2":3,"3":8,"4":5,"5":7,"6":6}
    
    # # 가장 cost가 작은 노드 값 구하기
    # def getShortNode(costs):
        
    #     return 0

    # # gate마다 dijkstra
    # for gate in gates:
    #     cur_v = gate
    #     cur_cost = 0 # 
    #     while cur_v not in summits:
    #         # cost가 가장 작은 key값
    #         costs = dijkstra(cur_v)
    #         cur_v = min(costs, key = costs.get)
    #         # intensity(cost중에 max(최대값)) 구하기
    #         if 'intensity' not in locals():
    #             intensity = costs[cur_v]
    #         else:
    #             intensity = max(intensity, costs[cur_v])
            
    #     min_summit = min(min_summit, cur_v)
        
    #     # min(intensity) 비교
    #     total_intensity = min(intensity, total_intensity)
    #     if 'intensity' not in locals():
    #             intensity = costs[cur_v]
    #         else:
        
    #     answer = [min_summit, total_intensity]
        
    # # dijkstra(start)의 가장 cost가 작은 노드를 찾아
    #     # intensity(max cost)저장
    #     # dijkstra(가장 cost 작은 노드)
    # # 가장 cost가 작은 노드가 summit이면 멈추기
    
    # # intensity가 가장 작으면 answer = [summit, intensity] 저장
    
    
    
    
    
    # # intensity 최소 등산코스 찾기
    #     # 산봉우리 번호 작은거 찾기
    # # 1 출발(gate) -> 5 산봉우리(summit) -> 1 출발(gate)
    # # dijkstra(1) -> dijkstra(2) -> dijkstra(4) -> dijkstra(6) -> dijkstra(5)
    
    
    

    # return answer # [산봉우리의 번호, intensity의 최솟값]


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
res = solution(n, paths, gates, summits)
print(res)