# Top-down
class Solution:
    def minCostClimbingStairs(self, cost):
        memo = {}
        n = len(cost)

        def dp(n):
            if n == 0 or n == 1:
                return 0
            if n not in memo:
                memo[n] = min(dp(n-2) + cost[n-2], dp(n-1) + cost[n-1])
            return memo[n]
        return dp(n)
        
        
sol = Solution()

cost1 = [10, 15, 20]
result1 = sol.minCostClimbingStairs(cost1)
print(result1) # 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result2 = sol.minCostClimbingStairs(cost2)
print(result2) # 6