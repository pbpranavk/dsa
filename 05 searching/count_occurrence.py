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

def count_occurrence(arr, x):
    n = len(arr)
    ind = binary_search_rec(arr, 0, n-1, x)

    if ind == -1:
        return 0

    count = 1
    left = ind -1
    while left >= 0 and arr[left] == x:
        count += 1
        left -= 1

    right = ind + 1
    while right < n and arr[right] == x:
        count += 1
        right += 1
    return count

print(count_occurrence([ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ], 2))