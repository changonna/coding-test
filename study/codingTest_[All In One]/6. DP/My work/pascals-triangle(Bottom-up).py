# https://leetcode.com/problems/pascals-triangle/
# Bottom-up

class Solution(object):
    def generate(self, numRows):
        memo = [[1] * i for i in range(1, numRows + 1)]
        for i in range(numRows):
            for j in range(i+1):
                if not (j == 0 or i == j):
                    memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
        return memo

sol = Solution()
answer = sol.generate(numRows = 5)
print(answer)