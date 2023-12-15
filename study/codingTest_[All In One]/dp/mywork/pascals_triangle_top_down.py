# https://leetcode.com/problems/pascals-triangle/
# Top-down

class Solution(object):
    def generate(self, numRows):
        memo = [[1] * i for i in range(1, numRows + 1)]
        def dp(numRows):
            # base case
            if numRows == 1 or numRows == 2:
                return memo[numRows - 1]
            
            # recursion
            prev_row = dp(numRows - 1)

            for i in range(1, numRows - 1):
                memo[numRows - 1][i] = prev_row[i-1] + prev_row[i]

            return memo[numRows - 1]
        dp(numRows)
        return memo

sol = Solution()
answer = sol.generate(numRows = 5)
print(answer)