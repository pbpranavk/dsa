import sys

def min_coins(coins, m, V):
    table = [0 for i in range(V + 1)]

    table[0] = 0

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]

coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print(min_coins(coins, m, V))