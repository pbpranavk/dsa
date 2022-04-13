def subarray_0_sum(arr):
    n = len(arr)
    n_sum = 0

    s = set()

    for i in range(n):
        n_sum += arr[i]

        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)

    return False

arr = [-3, 2, 3, 1, 6]
print(subarray_0_sum(arr))