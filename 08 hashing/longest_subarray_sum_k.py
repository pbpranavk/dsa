def longest_subarray(arr, k):
    n = len(arr)
    my_dict = {}
    sum = 0
    max_len = 0

    for i in range(n):
        sum += arr[i]

        if sum == k:
            max_len = i + 1
        elif sum - k in my_dict:
            max_len = max(max_len, i - my_dict[sum - k])

        if sum not in my_dict:
            my_dict[sum] = i

    return max_len

arr = [10, 5, 2, 7, 1, 9]
k = 15
print(longest_subarray(arr, k))