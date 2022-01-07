def left_rotate(arr, d):
    return arr[d-1:] + arr[:d-1]

print(left_rotate([1,2,3,4,5], 3))