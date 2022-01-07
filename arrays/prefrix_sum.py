def prefix_sum(arr):
    n = len(arr)
    prefix_sum_arr = [0 for i in range(n)]
    prefix_sum_arr[0] = arr[0]

    for i in range(1, n):
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i]

    return prefix_sum_arr

print(prefix_sum([10, 4, 16, 20 ]))