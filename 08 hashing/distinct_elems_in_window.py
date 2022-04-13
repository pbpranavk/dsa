#TODO: Recheck once again
from collections import defaultdict

def distinct_elems(arr, k):
    n =len(arr)

    mp = defaultdict(lambda:0)
    dist_count = 0
    for i in range(k):
        if mp[arr[i]] == 0:
            dist_count = 1
        mp[arr[i]] += 1
    print(dist_count)

    for i in range(k,n):
        if mp[arr[i - k]] == 1:
            dist_count -= 1
        mp[arr[i - k]] -= 1

        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1
        print(dist_count)

arr = [1, 2, 1, 3, 4, 2, 3]
distinct_elems(arr, 4)