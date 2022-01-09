def is_subsequence(s1, s2, m, n):
    if m == 0:
        return True

    if n == 0:
        return False

    if s1[m-1] == s2[n-1]:
        return is_subsequence(s1, s2, m-1, n-1)

    return is_subsequence(s1, s2, m, n-1)

s1 = "asdf"
s2 = "qwertpoiuasdfglkjhzxvcv"
print(is_subsequence(s1, s2, len(s1), len(s2)))