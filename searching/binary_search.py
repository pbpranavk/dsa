def binary_search_rec(arr, l, r, x):
    if r > l:
        mid = l + (r - 1) //2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_rec(arr, l, mid - 1, x)
        else:
            return binary_search_rec(arr, mid + 1, r, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
print(binary_search_rec(arr,0, len(arr) -1, 10))

def binary_search_iterative(arr, l, r, x):
    while l <= r:
        mid = l + (r - 1) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(binary_search_iterative(arr, 0, len(arr) -1, 10))