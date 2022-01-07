def square_root(number, precision):
    start = 0
    end, ans = number, 1

    while start <= end:
        mid = int((start + end) / 2)


        if mid * mid < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    increment = 0.1
    for i in range(0, precision):
        while ans * ans <= number:
            ans += increment

        ans = ans - increment
        increment = increment / 10
    return ans

print(round(square_root(50, 3), 4))
print(round(square_root(10, 4), 4))