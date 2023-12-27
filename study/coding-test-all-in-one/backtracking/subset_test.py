# 부분집합
# [1, 2, 3, 4]의 부분집합을 모두 구해 반환하시오

def solution(nums):
    answer = []

    def backtracking(start, curr):
        if len(curr) == k:
            answer.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()

    for k in range(len(nums) + 1):
        backtracking(start = 0, curr = [])
    return answer

nums = [1, 2, 3, 4]
print(solution(nums))