def trailing_zeros_of_factorial(n):
    if(n<0):
        return -1

    count = 0
    print("n is", n)
    while (n >= 5):
        n //= 5
        print("n is", n)
        count += n

    return count

print(trailing_zeros_of_factorial(100))