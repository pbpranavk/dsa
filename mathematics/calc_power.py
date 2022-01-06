def calc_power(x,y):
    temp = 0
    if (y ==0):
        return 1

    temp = calc_power(x, int( y / 2))

    if (y % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp

print(calc_power(5,9))