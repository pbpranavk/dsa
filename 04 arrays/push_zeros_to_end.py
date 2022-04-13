def push_zeros_to_end(arr):
    count = 0

    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
push_zeros_to_end(arr)
print(arr)