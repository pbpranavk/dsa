def longest_conseq_subseq(arr):
    n = len(arr)

    s = set()
    ans = 0

    for ele in arr:
        s.add(ele)

    for i in range(n):
        if (arr[i] - 1) not in s:
            j = arr[i]
            while j in s:
                j += 1
            ans = max(ans, j - arr[i])

    return ans

arr = [1, 9, 3, 10, 4, 20, 2]
print(longest_conseq_subseq(arr))
