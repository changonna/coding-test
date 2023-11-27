'''
# 기본 Graph_BFS 코드
start_v = rooms[0][0]
visited = [start_v]
queue = deque(start_v)

while queue:
    cur_v = queue.popleft()
    for v in rooms[cur_v]
        if v not in visited:
            queue.append(v)
            visited.append(v)
return visited
'''

from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        # 시작점 설정
        start_v = 0
        visited = [start_v]
        queue = deque()
        queue.append(start_v)

        while queue:
            roomNumber = queue.popleft()
            keys = rooms[roomNumber]
            for key in keys:
                if key not in visited:
                    queue.append(key)
                    visited.append(key)
        return len(visited) == len(rooms)

sol = Solution()
rooms1 = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms1)) # False
rooms2 = [[1],[2],[3],[0]]
print(sol.canVisitAllRooms(rooms2)) # True