'''
# 기본 Graph_DFS 코드
visited = []
def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
'''

from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = []
        def dfs(cur_v):
            visited.append(cur_v)
            for v in rooms[cur_v]:
                if v not in visited:
                    dfs(v)
        dfs(0)
        if len(visited) == len(rooms):
            return True
        else:
            return False