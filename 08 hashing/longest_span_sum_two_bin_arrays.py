def longest_span(arr1, arr2):
    n = len(arr1)
    arr = [0 for i in range(n)]

    for i in range(n):
        arr[i] = arr1[i] - arr2[i]

    hm = {}
    sum = 0
    max_len = 0

    for i in range(n):
        sum += arr[i]

        if sum == 0:
            max_len = i + 1
        if sum in hm:
            max_len = max(max_len, i - hm[sum])
        else:
            hm[sum] = i

    return max_len

arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
print(longest_span(arr1, arr2))