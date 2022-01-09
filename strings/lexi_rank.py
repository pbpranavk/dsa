MAX_CHARS= 256

count = [0] * (MAX_CHARS + 1)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n -1)

def populate_and_inc_count(str):
    for i in range(len(str)):
        count[ord(str[i])] += 1

    for i in range(MAX_CHARS):
        count[i] += count[i - 1]

def update_count(ch):
    for i in range(ord(ch), MAX_CHARS):
        count[i] -= 1


def find_rank(str):
    len1 = len(str)
    mul = fact(len1)
    rank = 1

    populate_and_inc_count(str)

    for i in range(len1):
        mul = mul // (len1 - i)
        rank += count[ord(str[i]) - 1] * mul
        update_count(str[i])

    return rank

print(find_rank("string"));