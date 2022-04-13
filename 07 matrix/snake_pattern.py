def snake_pattern(mat):
    rows = len(mat)
    cols = len(mat[0])

    for i in range(rows):

        if i % 2 == 0:
            for j in range(cols):
                print(mat[i][j], end = " ")
        else:
            for j in range(cols - 1, -1, -1):
                print(mat[i][j], end = " ")

mat = [[ 10, 20, 30, 40 ],
       [ 15, 25, 35, 45 ],
       [ 27, 29, 37, 48 ],
       [ 32, 33, 39, 50 ]]

snake_pattern(mat)