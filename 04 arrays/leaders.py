def leaders(arr):
    n = len(arr)

    max_from_right = arr[n-1]
    print(max_from_right, end=" ")
    for i in range(n-2, -1 ,-1):
        if max_from_right < arr[i]:
            print(arr[i], end=" ")
            max_from_right = arr[i]

leaders([16, 17, 4, 3, 5, 2])