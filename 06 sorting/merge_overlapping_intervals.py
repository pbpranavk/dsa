def merge_intervals(arr):
    arr = sorted(arr, key=lambda x: x[0])

    m = []
    s = -1000
    max = -1000

    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] > max:
                max = a[1]

    if max != -1000 and [s, max] not in m:
        m.append([s, max])

    return m

print(merge_intervals([[6, 8], [1, 9], [2, 4], [4, 7]]))
print(merge_intervals([[6, 8], [1, 5], [2, 4], [4, 7]]))
print(merge_intervals([[6, 8], [1, 5], [2, 4], [4, 5]]))
print(merge_intervals([[9, 11], [1, 5], [2, 4], [4, 5], [10, 15]]))
