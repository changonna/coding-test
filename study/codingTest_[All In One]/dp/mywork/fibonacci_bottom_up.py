memo = {
    1: 1,
    2: 1
}

def fibo(n):
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

answer = fibo(4)
print(answer)