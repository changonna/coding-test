## O(n) : newNumsionary

class Solution(object):
    def longestConsecutive(self, nums):
        newNums = set(nums)
        maxCnt = 0

        # dict = {}
        # for num in nums:
        #     dict[num] = 1

        for num in newNums:
            if num - 1 not in newNums:
                cnt = 1
                target = num + 1
                while target in newNums:
                    cnt += 1
                    target += 1
                maxCnt = max(cnt, maxCnt)
        return maxCnt

sol = Solution()
answer = sol.longestConsecutive(nums = [100, 4, 200, 1, 3, 2])
print(answer)
answer = sol.longestConsecutive(nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(answer)