def longest_even_odd_subarray(arr):
    n = len(arr)

    longest = 1
    cnt = 1

    for i in range(n-1):

        if((arr[i] + arr[i + 1]) % 2 == 1):
            cnt += 1
        else:
            longest = max(longest, cnt)
            cnt = 1

    if longest == 1:
        return 0

    return max(cnt, longest)

print(longest_even_odd_subarray([ 1, 2, 3, 4, 5, 7, 8 ]))
