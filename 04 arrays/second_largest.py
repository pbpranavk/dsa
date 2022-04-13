def second_largest(arr):
    n = len(arr)

    if n < 2:
        print("Invalid input")
        return

    largest = second = -2454635434

    for ele in arr:
        largest = max(ele, largest)

    for ele in arr:
        if ele != largest:
            second = max(ele, second)

    if(second != -2454635434):
        print(second)
    else:
        print("Not present")

second_largest([10, 1, 5, 15, 24, 2, 4])