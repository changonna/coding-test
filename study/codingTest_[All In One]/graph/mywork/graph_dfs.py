graph = { 
  'A': ['B', 'D', 'E'],
  'B': ['A', 'C', 'D'],
  'C': ['B'],
  'D': ['A' ,'B'],
  'E': ['A']
}

graph = {
  'A': ['B', 'E', 'H'],
  'B': ['A', 'C', 'D'],
  'C': ['B', 'K'],
  'D': ['A', 'B', 'F', 'G'],
  'E': ['A'],
  'F': ['D', 'I'],
  'G': ['D', 'J', 'K'],
  'H': ['A'],
  'I': ['F'],
  'J': ['G'],
  'K': ['C', 'G']
}
visited = []

def dfs(cur_v):
  visited.append(cur_v)
  for v in graph[cur_v]:
    if v not in visited:
      dfs(v) # 재귀


dfs('A')
print(visited)