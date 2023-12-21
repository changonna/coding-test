# 내가 푼 코드

'''
2022 KAKAO TECH INTERNSHIP
Level : 3
문제 : 등산코스 정하기
알고리즘 : dijkstra
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118669
'''

'''
n : 지점수 (1 ~ n)
gates : 출입구 번호 배열
summits: 산봉우리 번호 담긴 정수배열

2 <= n <= 50,000 = 5 * 10^4
n-1 <= paths(간선) <= 200,000 ≈ 2^18(262,144)

cost 최대 10,000,000 : 1 ≤ w ≤ 10,000,000

양방향
intensity : 가장 긴 시간을 해당 등산코스의 intensity

출입구(1) -> 원래 출입구(1)

출입구 -> 산봉우리 1곳 -> 원래 출입구

intensity 최소의 등산코스
'''

from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    # MAX는 보다 큰 값 설정
    MAX = 10000001
    answer = [0, MAX]

    # 0. summits을 list -> set으로 변경 : O(n)
    set_summits = set(summits)

    # 1. paths를 graph로 변경 (양방향)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    # 2. dijkstra algorithm
    min_dis = [MAX for _ in range(n+1)] # ! (n+1) 주의
    # 2.1 우선순위 큐에 시작노드 gates 한 번에 넣기
    pq = [(0, gate) for gate in gates]
    while pq:
        # 2.2 우선순위 가장 높은 노드 추출
        intensity, cur_v = heapq.heappop(pq)
        '''
        # 2.3 방문여부 확인
        # if cur_v not in costs:
        #     costs[cur_v] = intensity
        '''

        # 2.3 방문여부 확인 대신에 min_dis[cur_v]보다 intensity가 더 작은값이면 갱신
        if min_dis[cur_v] > intensity:
            # 2.4 비용 업데이트
            min_dis[cur_v] = intensity
        else: # 크거나 같으면 무시
            continue

        # 2.5 현재 노드와 연결된 노드 우선순위 큐에 추가
        for cost, next_v in graph[cur_v]:
            # 현재 cost와 다음 cost 비교해서 next_cost 구하기
            next_cost = max(intensity, cost)
            if min_dis[next_v] <= next_cost:
                continue
            # heappush 전에 산봉우리 노드 만나면 continue
            if cur_v in set_summits: # 탐색시 시간복잡도 줄이기 list=O(n) -> set=O(1)
                continue
            heapq.heappush(pq, (next_cost, next_v))

    # 3. summits 돌면서 answer 구하기
    for summit in summits:
        # min_dis(summit)이 최저 intensity보다 작으면
        if answer[1] > min_dis[summit]:
            answer = [summit, min_dis[summit]]
        # intensity가 같으면 산봉우리 번호가 작은 값 선택
        elif answer[1] == min_dis[summit] and summit < answer[0]:
            answer[0] = summit
    return answer



n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
res = solution(n, paths, gates, summits)
print(res)