def fib(n, a=0, b= 1):
    if n == 0:
        return a
    elif n == 1:
        return b
    return fib(n-1, b, a + b)

print(fib(13))