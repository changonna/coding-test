'''
level 2
dijkstra
배달(Delivery)
https://school.programmers.co.kr/learn/courses/30/lessons/12978
'''

'''
    가중치 그래프 + 최단경로 -> dijkstra
    
    # 노드(node) = 50 
    # road의 길이 = 간선(edge) = 2,000
    # 간선 하나당 최대 가중치(cost) 10,000
'''

from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    
    # 1. road를 graph로 변경
    # O(n) = O(2000)
    # graph = { i : [] for i in range(1, N+1) }
    graph = defaultdict(list)
    for n1, n2, cost in road:
        # 양방향이니까 양쪽으로 추가
        graph[n1].append((cost, n2))
        graph[n2].append((cost, n1))
    
    # 2. dijkstra algorithm
    # O(E log E) = O(2000 log 2000) = 2000 * log_2 2^11 = 2000 * 11 = 2.2 * 10^4
    costs = {} #(cost, node)
    pq = []
    heapq.heappush(pq, (0, 1))
    
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        
        if cur_node not in costs:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node)) 
                
    # 3. 배달 가능한 경우의 수 구하기
    # O(n) = O(50)
    for key in range(1, len(costs)+1):
        if costs[key] <= K:
            answer += 1
    
    return answer

# test1
road1 = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
res = solution(5, road1, 3)
print(res) # 4

# test2
road2 = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
res = solution(6, road2, 4)
print(res) # 4