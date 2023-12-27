def solution(nums, k):
    answer = []

    def backtracking(start, curr):
        if len(curr) == k:
            answer.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()

    backtracking(start = 0, curr = [])
    return answer


print(solution(nums = [1, 2, 3, 4], k = 3))