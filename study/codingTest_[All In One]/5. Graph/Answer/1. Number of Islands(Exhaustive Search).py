# Graph
# 완전탐색

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        number_of_islands = 0
        row = len(grid) # 4
        col = len(grid[0]) # 5
        visited = [[False] * col for _ in range(row)]

        def bfs(x, y):
           dx = [-1, 1, 0, 0]
           dy = [0, 0, -1, 1]

          # 방문한 값 True
           visited[x][y] = True
           # queue 선언 및 초기화
           queue = deque()
           queue.append((x, y))
           while queue:
              cur_x, cur_y = queue.popleft()
              for i in range(len(dx)):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                # next_x, next_y 범위 안넘게 / 
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                  if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

        # 완전탐색
        for i in range(row):
          for j in range(col):
            # 값이 1이고 방문하지 않았으면
            if grid[i][j] == '1' and not visited[i][j]:
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

grid2 = [
  ['1', '1', '1', '0', '0'],
  ['1', '1', '0', '0', '0'],
  ['1', '1', '0', '1', '0'],
  ['0', '0', '0', '0', '1']
]
print(sol.numIslands(grid1)) # 1
print(sol.numIslands(grid2)) # 3