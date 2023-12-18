# 참고할 강사 코드

from collections import deque
def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if not visited[next_v]:  # 방 번호가 0,1,2, ... , n-1 이라서 가능한 코드
                dfs(next_v)

    dfs(0)
    return all(visited)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRooms(rooms))