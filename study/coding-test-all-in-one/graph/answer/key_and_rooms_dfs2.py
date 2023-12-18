# ChatGPT 코드

from collections import deque

def canVisitAllRooms(rooms):
    n = len(rooms)
    visited = set()

    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)

    dfs(0)

    return len(visited) == n

rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRooms(rooms))