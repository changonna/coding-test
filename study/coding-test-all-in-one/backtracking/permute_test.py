def permute(nums):
    answer = []
    def backtracking(curr):
        if len(nums) == len(curr):
            answer.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtracking(curr)
                curr.pop()
    backtracking([])
    return answer

nums = [1, 2, 3, 4]
print(permute(nums))