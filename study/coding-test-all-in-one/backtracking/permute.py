# 순열
# Q. nums = [1, 2, 3, 4]로 만들 수 있는 모든 순열을 반환하시오

def permute(nums):
    # 재귀
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    ans = []
    backtrack([])
    return ans


# 재귀를 이용해서 모든 케이스를 방문하는 이 방법을 backtracking이라고 부르는 경우가 있다.
nums = [1, 2, 3, 4]
res = permute(nums)
print(res)