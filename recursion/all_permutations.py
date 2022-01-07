def all_permutations(a, l, r):
    if l == r:
        print("".join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            all_permutations(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

str = "ABC"
all_permutations(list(str), 0, len(str) - 1)
