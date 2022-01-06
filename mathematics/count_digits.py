import math

def count_digits_while(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

def count_digit_recursive(n):
    if n / 10 == 0:
        return 0
    return 1 + count_digit_recursive(n // 10)

def count_digit_log(n):
    return math.floor(math.log10(n) + 1)

def count_digit_str(n):
    return len(str(n))

n = 1234345456356
print(count_digits_while(n))
print(count_digit_recursive(n))
print(count_digit_log(n))
print(count_digit_str(n))
