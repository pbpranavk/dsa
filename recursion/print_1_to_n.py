def print_1_to_n_rec(n, N):
    if(n <= N):
        print(n, end=" ")
        print_1_to_n_rec(n + 1, N)

    return

def print_1_to_n(N):
    print_1_to_n_rec(1, N)


print_1_to_n(5)