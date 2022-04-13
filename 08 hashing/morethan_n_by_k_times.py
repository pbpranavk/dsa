def morethan_n_by_k_times(arr, k):
    n = len(arr)

    x = n // k

    freq = {}

    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    for i in freq:
        if freq[i] > x:
            print(i)

arr = [ 1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1 ]
k = 4
morethan_n_by_k_times(arr, k)