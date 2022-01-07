def check_sorted(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return True

    for i in range(1, n):
        if arr[i-1] > arr[i] :
            return False

    return True

print(check_sorted([10, 1, 5, 15, 24, 2, 4]))
print(check_sorted([6,7,9,10]))