'''
2. backtracking을 이용한 경우
재귀를 이용하여 구현
'''

# List [4, 9, 7, 5, 1]에서 2개의 숫자를 더해서 12가 될 수 있나요? (중복 X)

def solution(nums, target):
    def backtrack(start, curr):
        # base case : 2개의 합을 더해서 target과 같으면
        if len(curr) == 2 and sum(nums[i] for i in curr) == target:
            return curr

        # recursion : 
        for i in range(start, len(nums)):
            curr.append(i)
            res = backtrack(i + 1, curr)
            
            if res:
                return res
            
            curr.pop()
        return None
    return backtrack(0, [])

nums = [4, 9, 7, 5, 1]
print(solution(nums, 12))