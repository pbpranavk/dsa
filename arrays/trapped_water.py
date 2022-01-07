def trapped_water(arr):
    n = len(arr)

    left = 0
    right = n-1

    l_max = 0
    r_max = 0


    result = 0
    while left <= right:
        if r_max <= l_max:
            result += max(0, r_max - arr[right])
            r_max = max(r_max, arr[right])
            right -= 1
        else:
            result += max(0, l_max - arr[left])
            l_max = max(l_max, arr[left])
            left += 1
    return result

print(trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))