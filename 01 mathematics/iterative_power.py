def iterative_power(x, y):
    res = 1

    while (y > 0):
        if (y & 1 == 1):
            # y is odd therefore multiply with x
            res = res * x

        # y must be even now, therefore change y to y/2 and x to x^2
        y = y >> 1

        x = x * x
    return res

print(iterative_power(5,9))