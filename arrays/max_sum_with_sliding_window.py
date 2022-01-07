def max_sum_with_sliding_window(arr, k):
    n = len(arr)

    if n < k:
        print("Invalid")
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum_with_sliding_window([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))