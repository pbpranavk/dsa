def get_max_consecutive_ones_in_binary_array(arr):
    n = len(arr)
    count = 0

    result = 0

    for i in range(0, n):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            result = max(result, count)
    return result

print(get_max_consecutive_ones_in_binary_array([1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]))