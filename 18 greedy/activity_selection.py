def sorted_activity_selection(s, f):
    n = len(f)

    i = 0
    print(i, end = " ")

    for j in range(n):
        if s[j] >= f[i]:
            print(j, end = " ")
            i = j

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
sorted_activity_selection(s, f)

def unsorted_activity_selection(arr):
    n = len(arr)
    selected = []
    arr.sort(key = lambda x : x[1])
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected

activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
print(unsorted_activity_selection(activity))
