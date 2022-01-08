def rot_mat(mat):
    rows = len(mat)


    for x in range(0, int(rows / 2)):
        for y in range(x, rows - x - 1):
            temp = mat[x][y]
            mat[x][y] = mat[y][rows - 1 - x]
            mat[y][rows - 1 - x] = mat[rows - 1 - x][rows - 1 - y]
            mat[rows - 1 - x][rows - 1 - y] = mat[rows - 1 - y][x]
            mat[rows - 1 - y][x] = temp

    for i in range(rows):
        for j in range(rows):
            print(mat[i][j], end = " ")
        print("")

mat = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]

rot_mat(mat)