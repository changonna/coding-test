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

from collections import deque
class Solution():
    def numIslands(self, grid):
        number_of_islands = 0 # 섬의 총 개수
        # row, col 설정
        row = len(grid)
        col = len(grid[0])
        # visited 설정 = grid 크기 만큼 False로 만들기
        visited = [[False] * col for _ in range(row)]

        def bfs(x, y):
            # 상,하,좌,우 설정
            mx = [-1, 1, 0, 0]
            my = [0, 0, -1, 1]

            visited[x][y] = True # 방문한 좌표 visited True로 설정
            # queue 설정 및 초기화
            queue = deque()
            queue.append((x, y))

            while queue:
                cur_x, cur_y = queue.popleft() # Tuple Unpacking
                # mx, my 만큼 4번 돌리기
                for i in range(len(mx)):
                    # 현재 좌표에서 상,하,좌,우 좌표 구하기
                    next_x = cur_x + mx[i]
                    next_y = cur_y + my[i]

                    # 상,하,좌,우 테두리 설정
                    if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                        # 땅(1)이고 방문하지 않은
                        if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True # visited에 해당 좌표 True로 변환
                            queue.append((next_x, next_y)) # queue에 추가하여 이어진 1을 찾아 계속 실행하도록

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