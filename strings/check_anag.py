def check_anag(s1, s2):
    hm1 = {}
    hm2 = {}

    for elem in s1:
        if elem in hm1:
            hm1[elem] += 1
        else:
            hm1[elem] = 0

    for elem in s2:
        if elem in hm2:
            hm2[elem] += 1
        else:
            hm2[elem] = 0

    for k, v in hm1.items():
        if hm2[k] != v:
            return False

    return True

print(check_anag("malayalam", "mmaallyaa"))