def naive_pattern_matching(pat, txt):
    M = len(pat)
    N = len(txt)

    for i in range(N - M + 1):
        j = 0

        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1

        if j == M:
            print("Pattern found at: ", i)

naive_pattern_matching("AABA", "AABAACAADAABAAABAA")

d= 256
def rabin_karp_pattern_matching(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1

    for i in range(M-1):
        h = (h*d)%q

    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    for i in range(N - M + 1):
        if p == t :
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            if j == M:
                print("Pattern found at: ", str(i))

        if i < N - M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

            if t < 0:
                t += q
rabin_karp_pattern_matching("AABA", "AABAACAADAABAAABAA", 101)

def kmp_pattern_matching(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    j = 0

    compute_LPS_array(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M :
            print("Pattern found at: ", str(i - j))
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j !=0 :
                j = lps[j-1]
            else:
                i += 1

def compute_LPS_array(pat, M, lps):
    len = 0
    lps[0] = 0
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] =  len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

kmp_pattern_matching("AABA", "AABAACAADAABAAABAA")