def power_set(str, idx, curr):
    n = len(str)

    if idx == n:
        return

    print(curr, end=" ")

    for i in range(idx + 1, n):
        curr += str[i]
        power_set(str, i, curr)

        curr = curr.replace(curr[len(curr) - 1], "")

    return

power_set("abc", -1, "")