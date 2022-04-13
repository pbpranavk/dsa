def first(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid -1
    return res

def last(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res

arr= [ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
print("First occurrence: ", first(arr, 8))
print("Last occurrence: ", last(arr, 8))