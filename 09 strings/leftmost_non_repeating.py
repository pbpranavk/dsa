def leftmost_non_repeat(s):
    hm = {}

    for idx, ele in enumerate(s):
        if ele in hm:
            hm[ele]["count"] += 1
        else:
            hm[ele] = {"count" : 1, "idx": idx}


    vals = hm.values()
    sorted(vals,key = lambda x:x["idx"])

    for ele in vals:
        if ele["count"] == 1:
            return ele["idx"]

    return -1

s = "geeksforgeeks"
print(s[leftmost_non_repeat(s)])