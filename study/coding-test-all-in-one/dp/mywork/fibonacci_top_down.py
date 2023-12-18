# f(n)부터 f(1)로 접근하므로, top-down 방식
# 재귀(recursion)으로 구현
# memoization : Top-down 방식에서 memo를 채워 나가는 것

memo = {}

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if n not in memo:
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]