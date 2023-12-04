# Bottom-up
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)

        # list 초기화해서 영역 설정하기
        dp = [-1] * (n) 
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]

sol = Solution()

cost1 = [10, 15, 20]
result1 = sol.minCostClimbingStairs(cost1)
print(result1) # 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result2 = sol.minCostClimbingStairs(cost2)
print(result2) # 6