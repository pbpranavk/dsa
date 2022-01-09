NO_OF_CHARS = 256

def leftmost_repeating(s):

    visited = [False for _ in range(NO_OF_CHARS)]

    res = -1
    for i in range(len(s) -1 , -1, -1):
        if not visited[s.index(s[i])]:
            visited[s.index(s[i])] = True
        else:
            res = i
    return res

string = "geeksforgeeks"
index = leftmost_repeating(string)
print(string[index] if index != -1 else "Not found")