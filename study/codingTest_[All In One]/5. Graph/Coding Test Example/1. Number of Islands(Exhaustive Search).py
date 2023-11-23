# from collections import deque

# graph = {
#   'A': ['B'],
#   'B': ['A', 'C', 'E'],
#   'C': ['B', 'D'],
#   'D': ['C', 'E', 'F'],
#   'E': ['B', 'D', 'F'],
#   'F': ['D', 'E']
# }

# def graphBfs(start_v):
#     visited = [start_v]
#     queue = deque(start_v)

#     while queue:
#         cur_v = queue.popleft()
#         for v in graph[cur_v]:
#             if v not in visited:
#                 queue.append(v)
#                 visited.append(v)

#     return visited
    
# print(graphBfs('A'))



####

class Solution():
    def numIslands(self, grid):
        number_of_islands = 0
        # row, col 설정
        row = len(grid)
        col = len(grid[0])
        # visited 설정
        visited = [[False] * col for _ in range(row)]

        def bfs(x, y):
            # 상,하,좌,우 설정
            mx = [-1, 1, 0, 0]
            my = [0, 0, -1, 1]

            for i in range(len(mx)):
                # 현재 좌표에서 상,하,좌,우 좌표 구하기
                next_x = x + mx[i]
                next_y = y + my[i]

                # 상,하,좌,우 테두리 설정
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    # 땅(1)이고 방문하지 않은
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        # visited에 해당 좌표 True로 변환
                        visited[next_x][next_y] = True

        # 완전탐색
        for i in range(row):
            for j in range(col):
                # 땅(1)이고 방문하지 않은 
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

print(sol.numIslands(grid1))