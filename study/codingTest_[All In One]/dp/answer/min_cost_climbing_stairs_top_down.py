# Top-down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(n):
            if n == 0 or n == 1:
                return 0
            if n not in memo:
                memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
            return memo[n]

        result = dp(len(cost))
        return result