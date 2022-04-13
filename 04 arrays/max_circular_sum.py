def max_circular_sum(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    sum = 0
    for ele in range(n):
        sum += ele

    curr_max = arr[0]
    max_so_far = arr[0]
    curr_min = arr[0]
    min_so_far = arr[0]

    for i in range(1, n):
        curr_max = max(curr_max + arr[i], arr[i])
        max_so_far = max(max_so_far, curr_max)

        curr_min = min(curr_min + arr[i], arr[i])
        min_so_far = min(min_so_far, curr_min)

    if min_so_far == sum:
        return max_so_far

    return max(max_so_far, sum - min_so_far)

print(max_circular_sum([11, 10, -20, 5, -3, -5, 8, -13, 10]))