# 조합
# Q. nums = [1, 2, 3, 4]에서 두 개의 원소를 선택해 만들 수 있는 모든 조합을 반환하시오

def solution(nums, k):
    result = []

    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()
    backtracking(start = 0, curr = [])

    return result


print(solution(nums = [1, 2, 3, 4], k = 2))