def check_is_str_rotated(s, goal):
    if len(s) != len(goal):
        return False

    q1 = []
    for i in range(len(s)):
        q1.insert(0, s[i])

    q2 = []
    for i in range(len(goal)):
        q2.insert(0, goal[i])

    k = len(goal)
    while k > 0:
        ch = q2[0]
        q2.pop(0)
        q2.append(ch)
        if q2 == q1:
            return True

        k -= 1

    return False

s1 = "ABCD"
s2 = "CDAB"
s3 = "ACBD"
print(check_is_str_rotated(s1, s2))
print(check_is_str_rotated(s1, s3))