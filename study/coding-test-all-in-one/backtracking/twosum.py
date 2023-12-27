# List [4, 9, 7, 5, 1]에서 두 개의 숫자를 더해서 12가 될 수 있나요? (중복 X)

def solution(nums, target):
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]

nums = [4, 9, 7, 5, 1]
print(solution(nums, 15))