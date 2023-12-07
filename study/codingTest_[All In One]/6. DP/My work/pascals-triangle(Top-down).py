# https://leetcode.com/problems/pascals-triangle/
# Top-down

class Solution(object):
    def generate(self, numRows):
        memo = [[1] * i for i in range(1, numRows + 1)]
        
        return memo

# sol = Solution()
# answer = sol.generate(numRows = 5)
# print(answer)