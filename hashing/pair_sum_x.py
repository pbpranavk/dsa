def pair_sum(arr, sum):
    n = len(arr)
    s = set()

    for i in range(0, n):
        temp = sum - arr[i]
        if temp in s:
            return [ arr[i], temp]
        s.add(arr[i])

arr = [1, 4, 45, 6, 10, 8]
print(pair_sum(arr, 16))