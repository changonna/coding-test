# DP(bottom-up)
class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    memo = {
      1: 1,
      2: 2
    }
    for i in range(3, n+1):
      memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


sol = Solution()
answer = sol.climbStairs(n=4)
print(answer)

'''
1 -1> 1
2 -2> 2 1/1
3 -3> 2/1 1/1/1 1/2
4 -5> 2/2 2/1/1 1/2/1 1/1/2 1/1/1/1
5 -8> 2/2/1 2/1/2 1/2/2 1/1/2/1
'''