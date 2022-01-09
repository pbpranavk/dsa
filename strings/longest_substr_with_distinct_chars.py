def longest_unique_substr_len(str):
    seen = {}
    max_len = 0

    start = 0

    for end in range(len(str)):
        if str[end] in seen:
            start = max(start, seen[str[end]] + 1)

        seen[str[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len

print(longest_unique_substr_len("malayalam"))