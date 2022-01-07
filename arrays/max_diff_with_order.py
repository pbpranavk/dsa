# larger elem should appear after smaller elem

def max_diff(arr):
    n = len(arr)
    max_diff = arr[1] - arr[0]
    min_ele = arr[0]

    for i in range(1, n):
        if arr[i] - min_ele > max_diff:
            max_diff = arr[i] - min_ele

        if arr[i] < min_ele:
            min_ele = arr[i]

    return max_diff

print(max_diff([10, 1, 5, 15, 24, 2, 4]))