def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])

    ret_mat = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            ret_mat[i][j] = mat[j][i]

    for i in range(rows):
        for j in range(cols):
            print(ret_mat[i][j], end=" ")
        print("")

mat = [ [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
transpose(mat)
