t = [[0 for i in range(9)] for j in range(9)]

def un_kp(price, length, Max_len, n):

    if (n == 0 or Max_len == 0):
        return 0;


    if (length[n - 1] <= Max_len):
        t[n][Max_len] = max(price[n - 1] + un_kp(price, length, Max_len - length[n - 1], n),
                un_kp(price, length, Max_len, n - 1));
    else:
        t[n][Max_len] = un_kp(price, length, Max_len, n - 1);

    return t[n][Max_len];



price = [1, 5, 8, 9, 10, 17, 17, 20 ];
n =len(price);
length = [0]*n;
for i in range(n):
    length[i] = i + 1;
Max_len = n;
print(un_kp(price, length, n, Max_len));
