'''
1. 반복문을 사용한 경우
n개의 숫자를 더해서 target이 되는 경우는
for문이 n개 있어야 가능하다.
시간복잡도 매우 높음
'''

# List [4, 9, 7, 5, 1]에서 3개의 숫자를 더해서 12가 될 수 있나요? (중복 X)

def solution(nums, target):
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]

nums = [4, 9, 7, 5, 1]
print(solution(nums, 15))