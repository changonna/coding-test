class Solution(object):
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]
        memo[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if memo[r][c] == -1:
                    unique_paths = 0
                    if r-1 >= 0:
                        unique_paths += memo[r-1][c]
                    if c-1 >= 0:
                        unique_paths += memo[r][c-1]
                    memo[r][c] = unique_paths
        return memo[r][c]
    

sol = Solution()
answer = sol.uniquePaths(m=3, n=7)
print(answer) # 28