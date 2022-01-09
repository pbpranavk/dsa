#TODO: Redo once again
import sys

MAX = 1000;

memo = [[-1 for i in range(MAX)] for j in range(MAX)] ;

def solve_egg_drop(n, k):

    if (memo[n][k] != -1):
        return memo[n][k];

    if (k == 1 or k == 0):
        return k;

    if (n == 1):
        return k;

    min = sys.maxsize;
    res = 0;

    for x in range(1,k+1):
        res = max(solve_egg_drop(n - 1, x - 1), solve_egg_drop(n, k - x));
        if (res < min):
            min = res;

    memo[n][k] = min + 1;
    return min + 1;

n = 2;
k = 36;
print(solve_egg_drop(n, k));