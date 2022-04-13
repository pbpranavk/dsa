def check_digit_is_palindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev == n

print(check_digit_is_palindrome(1234143))
print(check_digit_is_palindrome(112233332211))