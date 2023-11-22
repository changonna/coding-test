# Graph
# 완전탐색

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        start_v = (0, 0)
        visited = [start_v]
        queue = deque(start_v)

        for i in len(grid):
            for j in len(grid[i]):
              print('a')    
            
        
        return cnt

grid = [
  ['1', '1', '1', '1', '0'],
  ['1', '1', '0', '1', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '0', '0', '0']
]

sol = Solution()
print(sol.numIslands(grid)) # 1