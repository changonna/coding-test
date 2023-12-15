# 완전탐색 O(n³)

class Solution:
    def longestConsecutive(self, nums):

        if not nums:
            return 0

        nums.sort() # O(NlogN)

        max_length = 1
        reference = nums[0] # O(1)
        count = 1
        reps = {}

        # O(N)
        for num in nums[1:]:
            if num in reps: # O(1)
                continue

            reps[num] = 0
            if num - reference == count:
                count += 1
            else:
                max_length = count if count > max_length else max_length
                reference = num
                count = 1

        max_length = count if count > max_length else max_length
        return max_length


sol = Solution()
answer = sol.longestConsecutive(nums = [100, 4, 200, 1, 3, 2])
print(answer)
answer = sol.longestConsecutive(nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(answer)
