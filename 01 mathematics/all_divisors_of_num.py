import math

def all_divisors_of_num(n):
    for i in range(1, int(math.sqrt(n) + 1)):

        if(n%i==0):
            if (n/i == i):
                print(i)
            else:
                print(i, n//i)

print(all_divisors_of_num(100))