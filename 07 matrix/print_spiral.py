#TODO: Needs rework

def print_spiral(mat):
    ans = []

    if len(mat) == 0:
        return ans

    rows = len(mat)
    cols = len(mat[0])

    seen = [[0 for i in range(cols)] for j in range(rows)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    r = 0
    c = 0
    di =0

    for i in range(rows * cols):
        ans.append(mat[r])
        seen[r][c] = True
        cr = r + dr[di]
        cc = c + dc[di]


        if(0 <= cr and cr < rows and 0 <= cc and cc < cols and not(seen[cr][cc])):
            r = cr
            c = cc
        else:
            di = (di + 1) % 4
            r += dr[di]
            c += dc[di]

    return ans

mat = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

for x in print_spiral(mat):
    print(x, end=" ")
print()