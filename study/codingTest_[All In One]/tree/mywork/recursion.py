def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

answer = factorial(4)
print(answer)

def fibo(n):
    # if n == 1 or 2:
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(5))
