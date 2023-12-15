# 2. ShortestPathInBinarytMatrix1 보완
from collections import deque

class Solution(object):
  def shortestPathBinaryMatrix(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid)

    # 출발지나 목적지가 1이면 실패
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
      return -1

    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    queue = deque()
    queue.append((0, 0, 1))
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    while queue:
      cur_x, cur_y, cur_cnt = queue.popleft()

      # 목적지에 도착했으면
      if cur_x == n-1 and cur_y == n-1:
        return cur_cnt

      for i in range(len(dx)):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
          if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
            queue.append((next_x, next_y, cur_cnt + 1))
            visited[next_x][next_y] = True
              
    return -1

grid1 = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]
grid2 = [[0]]
grid3 = [[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]

sol = Solution()
print(sol.shortestPathBinaryMatrix(grid1)) # 4
print(sol.shortestPathBinaryMatrix(grid2)) # 1
print(sol.shortestPathBinaryMatrix(grid3)) # 25