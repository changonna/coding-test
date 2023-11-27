'''
개선된 코드
1. visited : List에서 set()으로 변경 + append() -> add()
2. queue 초기화 간소화
3. start_v 시작점 변수를 사용하지 않고 0으로 사용하는 것이 더 간결하다.
4. 
'''

from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set() # List를 set()으로 변경
        queue = deque([0]) # 선언시 초기화

        while queue:
            roomNumber = queue.popleft()
            keys = rooms[roomNumber]
            for key in keys:
                if key not in visited:
                    queue.append(key)
                    visited.add(key) # list.append를 set.add로 변경
        return len(visited) == len(rooms)

sol = Solution()
rooms1 = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms1)) # False
rooms2 = [[1],[2],[3],[0]]
print(sol.canVisitAllRooms(rooms2)) # True