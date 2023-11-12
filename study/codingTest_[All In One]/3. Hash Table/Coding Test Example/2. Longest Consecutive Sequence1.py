## O(n) : Dictionary

class Solution(object):
    def longestConsecutive(self, nums):
        memo = {}
        maxCnt = 0

        ## O(n)
        for num in nums:
            memo[num] = 1

        ## O(n)
        for num in nums:
            cnt = 1
            target = num + 1
            if num - 1 not in memo:
                # 최대 n번만
                while target in memo: # [in] Dictionary : O(1)
                    cnt += 1
                    target += 1
            cnt = max(cnt, maxCnt)
            if maxCnt < cnt:
                maxCnt = cnt
        return maxCnt


sol = Solution()
answer = sol.longestConsecutive(nums = [100, 4, 200, 1, 3, 2])
print(answer)
answer = sol.longestConsecutive(nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(answer)
