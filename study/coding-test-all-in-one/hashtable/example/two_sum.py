# 전에 List로 풀었던 문제를
# HashTable 을 사용하여 문제 풀이

'''
(문제) Two sum
정수가 저장된 배열 nums가 주어졌을 때,
nums의 원소중 두 숫자를 더해서
target이 될 수 있으면 True 불가능하면 False를 반환하세요.
같은 원소를 두 번 사용할 수 없습니다.

(제약조건)
2 <= nums.length <= 10⁴
-10⁹ <= nums[i] <= 10⁹
-10⁹ <= target <= 10⁹

(예시 1)
input: nums = {4, 1, 9, 7, 5, 3, 16}, target : 14
output : True

(예시 2)
input: nums = {2, 1, 5, 7}, target : 4
output : False
'''

class Solution(object):
    def twoSum(nums, target):
        memo = {}
        # O(n)
        for v in nums:
            memo[v] = True # O(1)
        # O(n)
        for v in nums:
            needed_number = target - v
            if needed_number in memo and needed_number != v: # O(1)
                return True
        return False

sol = Solution()
print(sol.twoSum(nums = [4, 1, 9, 7, 5, 3, 16], target = 14)) # True
print(sol.twoSum(nums = [2, 1, 5, 7], target = 14)) # False