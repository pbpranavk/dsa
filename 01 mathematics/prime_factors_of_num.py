import math

def prime_factors(n):
    while n % 2 == 0:
        print(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2 ): # 3 to sqrt of n with a step of 2 (i.e i += 2)
        while n % i == 0:
            print(i)
            n = n / i

    if(n > 2):
        print(n)

print(prime_factors(315))