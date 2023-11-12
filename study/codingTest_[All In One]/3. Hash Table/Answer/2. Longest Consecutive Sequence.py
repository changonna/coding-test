class Solution(object):
  def longestConsecutive(self, nums):
    longest = 0
    num_dict = {}
    # O(n)
    num_dict = set(nums)
    # for num in nums:
    #   num_dict[num] = True
    # O(n)
    for num in nums:
      if num-1 not in num_dict: # O(1) # 이전값이 있으면 의미가 없으므로 pass
        cnt = 1
        target = num + 1
        while target in num_dict: # O(1) # target 값이 있는지 확인
          target += 1
          cnt += 1
        longest = max(longest, cnt)
    return longest

      




    

    
sol = Solution()
answer = sol.longestConsecutive(nums = [100, 4, 200, 1, 3, 2])
print(answer)
answer = sol.longestConsecutive(nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(answer)
