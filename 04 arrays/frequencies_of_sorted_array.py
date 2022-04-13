def count_occurrences(arr, x):

    res = 0
    for ele in arr:
        if ele == x:
            res += 1
    return res

print(count_occurrences([1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8], 2))