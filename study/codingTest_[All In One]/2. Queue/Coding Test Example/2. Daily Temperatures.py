class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures) # 모두 0으로 초기화
        idx = 0

        for temp in temperatures:
            while stack and temp > stack[-1][0]:
                itemIdx = stack.pop()[1]
                cnt = idx - itemIdx
                answer[itemIdx] = cnt
            stack.append([temp, idx])
            idx += 1
        return answer

solution = Solution()
answer = solution.dailyTemperatures([71, 69, 67, 65, 69, 69, 71])
print(answer)
