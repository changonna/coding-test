# 1. Graph 기본 bfs 
# 인접리스트를 사용
from collections import deque

graph = {
  'A': ['B'],
  'B': ['A', 'C', 'E'],
  'C': ['B', 'D'],
  'D': ['C', 'E', 'F'],
  'E': ['B', 'D', 'F'],
  'F': ['D', 'E']
}

def bfs(start_v):
  visited = [start_v]
  queue = deque(start_v)

  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]:
      if v not in visited:
        visited.append(v)
        queue.append(v)
  
  return visited

print(bfs('A'))

# 2. 섬의 개수 구하기 문제
# 암시적 그래프 / bfs 사용
class Solution():
    def numIslands(self, grid):
        number_of_islands = 0
        row = len(grid) # 4
        col = len(grid[0]) # 5
        visited = [[False] * col for _ in range(row)]

        def bfs(x, y):
            mx = [-1, 1, 0, 0]
            my = [0, 0, -1, 1]
            queue = deque()
            queue.append((x, y))

            while queue:
                visited[x][y] = True
                cur_x, cur_y = queue.popleft()
                for i in range(len(mx)):
                    next_x = cur_x + mx[i]
                    next_y = cur_y + my[i]
                    
                    if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            queue.append((next_x, next_y))
                        
        for i in range(row):
            for j in range(col):
                # 땅(1)이고 visited 값이 0
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    number_of_islands += 1
        return number_of_islands


sol = Solution()

grid1 = [
  ['1', '1', '1', '1', '0'],
  ['1', '1', '0', '1', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '0', '0', '0']
]

grid1 = [
    ["1"],
    ["1"]
]

print(sol.numIslands(grid1))