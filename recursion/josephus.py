def jo(n, k):
    if n == 1:
        return 1

    return (jo(n-1 , k) + (k - 1)) % n + 1

print(jo(14, 2))