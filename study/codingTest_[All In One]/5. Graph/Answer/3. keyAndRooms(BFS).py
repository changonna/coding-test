from collections import deque


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)
    return all(visited)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRooms(rooms))