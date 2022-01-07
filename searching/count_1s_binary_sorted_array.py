def count_1s_binary_sorted_array(arr):
    n = len(arr)

    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < 1:
            high = mid - 1
        elif arr[mid] > 1:
            low = mid + 1
        else:
            if(mid == n-1 or arr[mid + 1] != 1):
                return mid + 1
            else:
                low = mid + 1
    return 0

print(count_1s_binary_sorted_array([ 1, 1, 1, 1, 0, 0, 0 ]))