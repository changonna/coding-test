# DP(Top-down)

class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    memo = {}

    if n == 1:
      return 1
    if n == 2:
      return 2

    if n not in memo:
      memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return memo[n]


sol = Solution()
answer = sol.climbStairs(n=35)
print(answer)

'''
1 -1> 1
2 -2> 2 1/1
3 -3> 2/1 1/1/1 1/2
4 -5> 2/2 2/1/1 1/2/1 1/1/2 1/1/1/1
5 -8> 2/2/1 2/1/2 1/2/2 1/1/2/1
6 -> 2/2/2 2/2/1/1 
'''