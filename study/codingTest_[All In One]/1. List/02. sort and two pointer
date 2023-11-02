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

# 시간복잡도 : O(n log n)
# 1번과 문제는 동일하지만 풀이 방법을 바꿔서
# 정렬(sort)하고 2개의 pointer로 줄여서 풀이

def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if(nums[l] + nums[r] == target):
            return True
        elif(nums[l] + nums[r] > target):
            r -= 1
        elif(nums[l] + nums[r] < target):
            l += 1
    return False

print(twoSum(nums = [4, 1, 9, 7, 5, 3, 16], target = 14))
print(twoSum(nums = [2, 1, 5, 7], target = 14))