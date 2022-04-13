def toh(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return

    toh(n-1, from_rod, aux_rod, to_rod)
    print("Move disk ",n , "from rod", from_rod, " to rod ", to_rod)
    toh(n-1,  aux_rod, to_rod, from_rod)

toh(3, "A", "C", "B")