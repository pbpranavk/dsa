from sys import maxsize

def max_subarray_sum(arr):
    size = len(arr)

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))

max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3])