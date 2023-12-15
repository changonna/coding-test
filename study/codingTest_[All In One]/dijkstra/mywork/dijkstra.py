import heapq

def dijkstra(graph, start, final):
    costs = {}
    pq = []
    # 1. 우선순위큐에 시작노드 추가
    heapq.heappush(pq, (0, start))

    while pq:
        # 2. 우선순위 가장 높은 노드 추출
        cur_cost, cur_v = heapq.heappop(pq)

        # 3. 방문여부 확인
        if cur_v not in costs:
            # 4. 비용 업데이트
            costs[cur_v] = cur_cost
            
            # 5. 현재 노드와 연결된 노드 우선순위 큐에 추가
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    # 6. 목적지에 기록된 비용 반환
    return costs[final]

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}

res = dijkstra(graph, 1, 8)
print(res) # 11 