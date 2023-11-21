from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    q = deque(start_v)
    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited