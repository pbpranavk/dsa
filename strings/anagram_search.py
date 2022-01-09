MAX = 256

def compare(arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True

def search(pat, txt):
    M = len(pat)
    N = len(txt)

    countP = [0] * MAX
    countTW = [0] * MAX

    for i in range(M):
        countP[ord(pat[i])] += 1
        countTW[ord(txt[i])] += 1

    for i in range(M, N):
        if compare(countP, countTW):
            print("Found at", i - M)


        countTW[ord(txt[i])] += 1
        countTW[ord(txt[i - M])] -= 1

    if compare(countP, countTW):
        print("Found at",N - M)

txt = "BACDGABCDA"
pat = "ABCD"
search(pat, txt)