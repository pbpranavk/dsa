# Revisit the non dp problem
# Revisit the dp approach as well

def ispallindrome(input, start, end):
    while (start < end):
        if (input[start] != input[end]):
            return False;
        start += 1
        end -= 1
    return True;

def convert(a, b):
    return str(a) + str(b);

def minpalparti_memo(input, i, j, memo):

    if (i > j):
        return 0;

    ij = convert(i, j);

    if (ij in memo):
        return memo[ij];

    if (i == j):
        memo[ij] = 0;
        return 0;
    if (ispallindrome(input, i, j)):
        memo[ij] = 0;
        return 0;

    minimum = 1000000000
    for k in range(i, j):
        left_min = 1000000000
        right_min = 1000000000
        left = convert(i, k);
        right = convert(k + 1, j);

        if (left in memo):
            left_min = memo[left];

        if (right in memo):
            right_min = memo[right];

        if (left_min == 1000000000):
            left_min = minpalparti_memo(input, i, k, memo);
        if (right_min == 1000000000):
            right_min = minpalparti_memo(input, k + 1, j, memo);

        minimum = min(minimum, left_min + 1 + right_min);

    memo[ij] = minimum;

    return memo[ij];

input = "ababbbabbababa";
memo = dict()
print(minpalparti_memo(input, 0, len(input) - 1, memo))
