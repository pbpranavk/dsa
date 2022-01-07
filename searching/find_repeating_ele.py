def find_repeating_ele(arr, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] != arr[mid + 1]:
        if mid > 0 and arr[mid - 1] == arr[mid]:
            return mid

        return find_repeating_ele(arr, low, mid-1)

    return find_repeating_ele(arr,  mid+1, high)

arr = [1, 2, 3, 3, 4, 5]
index = find_repeating_ele(arr, 0 , len(arr) - 1)

print(arr[index] if index != -1 else "Not present")

