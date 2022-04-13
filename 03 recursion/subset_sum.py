def sub_sum(arr, n , i, sum, count):
    if i == n:
        if sum == 0:
            count += 1
        return count

    count = sub_sum(arr, n, i + 1, sum - arr[i], count)
    count = sub_sum(arr, n, i + 1, sum, count)

    return count

arr = [1,2,3,4,5]
print(sub_sum(arr, len(arr), 0, 10, 0))