# 부분집합 : 조합의 코드를 조금만 바꾸면
# Q. nums = [1, 2, 3, 4]로 만들 수 있는 모든 부분집합을 모두 반환하시오
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
    # for문 돌려서 모든 부분집합 추가
    for k in range(len(nums) + 1):
        backtracking(start = 0, curr = [])
    return answer


print(solution(nums = [1, 2, 3, 4]))