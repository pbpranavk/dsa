#TODO: Needs re understanding
from bisect import bisect_right as upper_bound

MAX = 100;

def binary_median(m, r, d):
    mi = m[0][0]
    mx = 0

    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d-1] > mx :
            mx =  m[i][d-1]

    desired = (r * d + 1) // 2

    while (mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0];

        for i in range(r):
             j = upper_bound(m[i], mid)
             place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    print ("Median is", mi)
    return

r, d = 3, 3

m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
binary_median(m, r, d)
