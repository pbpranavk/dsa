N = 4

def print_sol(sol):
    for i in sol:
        for j in i:
            print(str(j), end = " ")
        print("")

def is_safe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

def solve_maze(maze):
    print("qwert")
    sol = [ [ 0 for j in range(4)] for i in range(4)]

    if solve_maze_util(maze, 0, 0, sol) == False:
        print("Soln doesn't exist")
        return False

    print_sol(sol)
    return True

def solve_maze_util(maze, x, y, sol):
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if is_safe(maze, x, y):

        if sol[x][y] == 1:
            return False

        sol[x][y] = 1

        if solve_maze_util(maze, x + 1, y , sol):
            return True

        if solve_maze_util(maze, x , y + 1, sol):
            return True

        if solve_maze_util(maze, x - 1, y, sol):
            return True

        if solve_maze_util(maze, x, y - 1, sol):
            return True

        sol[x][y] = 0
        return False

maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
solve_maze(maze)