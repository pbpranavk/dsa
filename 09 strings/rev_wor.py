def rev_wrd(s, w):
    l = s.split(" ")
    x  = []
    for ele in l:
        if ele == w:
            x.append(ele[::-1])
        else:
            x.append(ele)

    return " ".join(x)

print(rev_wrd("i love coding", "love"))