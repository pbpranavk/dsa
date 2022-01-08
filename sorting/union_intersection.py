def union_of_sorted_arrays(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0


    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end= " ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j], end= " ")
            j += 1
        else:
            print(arr2[j], end= " ")
            i += 1
            j += 1

    while i < m:
        print(arr1[i], end= " ")
        i += 1

    while j < n:
        print(arr2[j], end= " ")
        j += 1

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
union_of_sorted_arrays(arr1, arr2)

print(" ")

def intersection_of_sorted_arrays(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0


    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j], end= " ")
            i += 1
            j += 1
intersection_of_sorted_arrays(arr1, arr2)
