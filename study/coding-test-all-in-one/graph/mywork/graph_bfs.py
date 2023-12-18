# graph bfs(Breedth-First Search)
from collections import deque

def graphBfs(graph, start_v):
  # 초기설정
  visited = [start_v]
  queue = deque(start_v)

  while queue:
    cur_v = queue.popleft() # 현재 정점(v)
    for v in graph[cur_v]: # 해당 그래프의 값들을 돌면서
      if v not in visited: # 방문하지 않은 노드이면
        # visited와 queue에 append
        visited.append(v)
        queue.append(v)
  return visited

# 인접 리스트 (dictionary 사용)
graph = {
  'A': ['B'],
  'B': ['A', 'C', 'E'],
  'C': ['B', 'D'],
  'D': ['C', 'E', 'F'],
  'E': ['B', 'D', 'F'],
  'F': ['D', 'E']
}

print(graphBfs(graph, 'A'))