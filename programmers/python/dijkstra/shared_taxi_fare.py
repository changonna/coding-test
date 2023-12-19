'''
level 3
dijkstra
합승 택시 요금
https://school.programmers.co.kr/learn/courses/30/lessons/72413
'''

'''
n : 지점의 개수
s : 출발지점
a : A의 도착지점
b : B의 도착지점 
fares : 지점 사이의 예상 택시요금
'''

from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    answer = 0
    
    # 1. fares -> graph로 변경 (양방향)
    graph = defaultdict(list)
    for n1, n2, cost in fares:
        graph[n1].append((cost, n2)) # (cost, node)
        graph[n2].append((cost, n1))
    # return graph
        
    # 2. dijkstra 알고리즘 사용
    def dijkstra(start):
        costs = {}
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_node))
        return costs
    
    costsS = dijkstra(s)
    costsA = dijkstra(a)
    costsB = dijkstra(b)
    
    # 3. 총 비용의 합 구하기 : O(V)
    # 초기 answer 값 : S에서 시작한 A와 B의 비용 합
    answer = costsS[a] + costsS[b]

    # for i in range(1, n + 1):
    #     if i in costsS.keys():
    #         answer = min(answer, (costsS[i] + costsA[i] + costsB[i]))
    for i in costsS.keys():
        answer = min(answer, (costsS[i] + costsA[i] + costsB[i]))

    return answer