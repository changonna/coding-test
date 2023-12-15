# 개선한 코드
# 1. visited를 List가 아닌 set()으로 변경하여 append -> add
# 2. return시 if 조건문 제거

from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set() # set()
        def dfs(roomNumber):
            visited.add(roomNumber) # add
            for v in rooms[roomNumber]:
                if v not in visited:
                    dfs(v)
        dfs(0)
        return len(visited) == len(rooms) # 조건문 삭제

sol = Solution()
rooms1 = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms1)) # False
rooms2 = [[1],[2],[3],[0]]
print(sol.canVisitAllRooms(rooms2)) # True