def is_pali(str, s, e):
    if s == e:
        return True

    if(str[s] != str[e]):
        return False

    if(s < e+1):
        return is_pali(str, s + 1, e -1)

    return True

def is_palindrome_driver(str):
    n = len(str)

    if n == 0:
        return True

    return is_pali(str, 0, n - 1)


print(is_palindrome_driver("madam"))
print(is_palindrome_driver("adam"))