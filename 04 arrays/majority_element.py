def majority_element(arr):
    n = len(arr)

    arr.sort()

    count, max_ele, temp, f = 1, -1, arr[0], 0

    for i in range(1, n):
        if temp == arr[i]:
            count += 1
        else:
            count = 1
            temp = arr[i]

        if max_ele < count:
            max_ele = count
            ele = arr[i]

            if max_ele > n // 2:
                f = 1
                break
    if f == 1:
        return ele
    else:
        return -1

print(majority_element([1, 1, 2, 1, 3, 5, 1]))