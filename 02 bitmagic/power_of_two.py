def is_power_of_two(x):
    return x and (not (x & (x -1)))

print(is_power_of_two(32))
print(is_power_of_two(65))