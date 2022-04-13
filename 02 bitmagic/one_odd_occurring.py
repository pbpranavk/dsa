def get_odd_occurrence(arr):
    res = 0
    for ele in arr:
        res = res ^ ele

    return res
print(get_odd_occurrence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]))