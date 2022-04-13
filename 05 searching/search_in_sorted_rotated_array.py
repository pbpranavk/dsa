def binary_search(arr, l, r, x):
    if r > l:
        mid = l + (r - 1) //2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

def find_pivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid < low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid -1)
    return find_pivot(arr, mid + 1, high)

def pivoted_binary_search(arr, key):
    n = len(arr)

    pivot = find_pivot(arr, 0, n-1)

    if pivot == -1:
        return binary_search(arr, 0, n-1, key)

    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr, pivot+1, n-1, key)

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
print(pivoted_binary_search(arr, 3))