# Top-down
class Solution:
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]

        def dp(r, c):
            if r == 0 and c == 0:
                memo[r][c] = 1
                return memo[r][c]

            if memo[r][c] == -1:
                unique_paths = 0
                if (r - 1) >= 0:
                    unique_paths += dp(r - 1, c)
                if (c - 1) >= 0:
                    unique_paths += dp(r, c - 1)
                memo[r][c] = unique_paths
            return memo[r][c]

        return dp(m - 1, n - 1)