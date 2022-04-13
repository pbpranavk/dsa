def check_kth_bit_is_set(n, k):
    return n & (1 << (k - 1)) == 1

print(check_kth_bit_is_set(8, 1))
print(check_kth_bit_is_set(5, 1))