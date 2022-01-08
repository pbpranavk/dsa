def lomuto_partition(arr, low, high):
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def hoares_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1

        while arr[i] < pivot:
            i += 1

        j -= 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        # pi = lomuto_partition(arr, low, high)
        pi = hoares_partition(arr, low, high)

        # quick_sort(arr, low, pi -1) # for lomuto
        quick_sort(arr, low, pi) # for hoare
        quick_sort(arr,  pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0 , len(arr) - 1)
print(arr)