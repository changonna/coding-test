# bfs

from collections import deque


class Solution:
    def isInRange(self, r, c, row_len, col_len):
        return (r >= 0 and r < row_len) and (c >= 0 and c < col_len)

    def shortestPathBinaryMatrix(self, grid):
        shortest_dist = -1
        row_len = len(grid)
        col_len = len(grid[0])
        if (
            grid[0][0] == 1 or grid[row_len - 1][col_len - 1] == 1
        ):  # 목적지는 이렇게 안해도 되긴함. 그런데 시간을 아낄 수 있음
            return shortest_dist

        visited = [[False] * col_len for _ in range(row_len)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True
        while queue:
            cur_r, cur_c, cur_dist = queue.popleft()
            if cur_r == row_len - 1 and cur_c == col_len - 1:
                shortest_dist = cur_dist
                break
            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if self.isInRange(next_r, next_c, row_len, col_len):
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_dist + 1))
                        visited[next_r][next_c] = True

        return shortest_dist
        


grid1 = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]

sol = Solution()
print(sol.shortestPathBinaryMatrix(grid1))