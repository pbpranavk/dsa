def fin_min_diff(arr):
    n = len(arr)
    arr = sorted(arr)

    diff = 10 ** 20

    for i in range(n-1):
        diff = min(diff, arr[i+1] - arr[i])

    return diff

print(fin_min_diff([1, 5, 3, 19, 18, 25]))