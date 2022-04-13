def pair_sum(arr, x):
    n = len(arr)
    i = 0
    j = n -1

    while i < j:
        if arr[i] + arr[j] == x:
            return True

        elif arr[i] + arr[j] < x:
            i += 1
        else:
            j -= 1
    return False

arr = [2, 3, 5, 8, 9, 10, 11]

x = 17
print(pair_sum(arr, x))
print(pair_sum(arr, 77))