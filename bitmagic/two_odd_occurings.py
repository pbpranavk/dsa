def two_odd_occurrings(arr):
    size = len(arr)

    xor2 = arr[0]
    set_bit_no = 0
    n = size - 2
    x, y = 0, 0

    for ele in arr:
        xor2 = xor2 ^ ele

    set_bit_no = xor2 & ~(xor2 - 1)

    for ele in arr:
        if (ele & set_bit_no):
            x = x ^ ele
        else:
            y = y ^ ele
    return [x, y]
print(two_odd_occurrings([4, 2, 4, 5, 2, 3, 3, 1]))