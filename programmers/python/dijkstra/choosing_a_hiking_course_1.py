# 참고 코드 (https://www.youtube.com/watch?v=xLG6e4ov9dY)

'''
2022 KAKAO TECH INTERNSHIP
Level : 3
문제 : 등산코스 정하기
알고리즘 : dijkstra
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118669
'''

from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    summits = set(summits)
    conn = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        conn[i].append((j, w))
        conn[j].append((i, w))

    # dijkstra
    pq = [(0, gate) for gate in gates] # (현재 경로까지의 intensity, 현재 지점)

    MAX = 10000001
    min_dis = [MAX for _ in range(n + 1)]

    while pq:
        intensity, node = heapq.heappop(pq)
        if min_dis[node] <= intensity:
            continue
        min_dis[node] = intensity

        # 현재 노드가 산봉우리면 더이상 진행하지 않음
        if node in summits:
            continue

        for nxt, nxt_w in conn[node]:
            nxt_w = max(intensity, nxt_w)
            if min_dis[nxt] <= nxt_w:
                continue
            heapq.heappush(pq, (nxt_w, nxt))

    # print(min_dis) # [MAX, 0, 3, 0, 3, 3, 3]
    answer = [0, MAX] # (산봉우리 번호, intensity 최솟값)

    for summit in summits:
        if min_dis[summit] < answer[1]:
            answer = [summit, min_dis[summit]]
        elif min_dis[summit] == answer[1] and summit < answer[0]:
            answer[0] = summit
    return answer

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
res = solution(n, paths, gates, summits)
print(res)