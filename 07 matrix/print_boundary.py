def print_boundary(mat):
    rows = len(mat)
    cols = len(mat[0])

    for i in range(rows):
        for j in range(cols):
            if i == 0:
                print(mat[i][j], end = " ")
            elif i == rows - 1:
                print(mat[i][j], end = " ")
            elif j == 0:
                print(mat[i][j], end = " ")
            elif j == cols - 1:
                print(mat[i][j], end = " ")
            else:
                print(" ", end= " ")
        print("")

a = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ],
    [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ]

print_boundary(a)