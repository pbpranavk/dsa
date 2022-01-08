def largest_subseq(arr):
    n = len(arr)

    hm = {}
    curr_sum = 0
    max_len = 0
    ending_index = -1

    for i in range(0,n):
        if arr[i] == 0:
            arr[i] = -1
        else:
            arr[i] = 1

    for i in range(0, n):
        curr_sum += arr[i]

        if curr_sum == 0:
            max_len = i + 1
            ending_index = i

        if curr_sum in hm:
            if max_len < i - hm[curr_sum]:
                max_len = i - hm[curr_sum]
        else:
            hm[curr_sum] = i
    for i in range(0,n):
        if arr[i] == -1:
            arr[i] = 0
        else:
            arr[i] = 1

    print (ending_index - max_len + 1, end =" ")
    print ("to", end = " ")
    print (ending_index)

    return max_len

arr = [1, 0, 0, 1, 0, 1, 1]
largest_subseq(arr)