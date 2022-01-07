def natural_number_sum(n):
    if (n <= 1 ):
        return n

    return n + natural_number_sum(n-1)

print(natural_number_sum(10))