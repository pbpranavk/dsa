N = 100000

tree = [0] * (2 * N)

def build(arr):
    for i in range(n):
        tree[n + i] = arr[i]

    for i in range(n-1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]

def update_tree_node(p, value):
    tree[p + n] = value
    p += n

    i = p

    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1

def query(l, r):
    res = 0

    l += n
    r += n

    while l < r:
        if l & 1:
            res += tree[l]
            l += 1
        if r & 1:
            r -= 1
            res += tree[r]

        l >>= 1
        r >>= 1
    return res

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
# n is global
n = len(a);
# build tree
build(a);
# print the sum in range(1,2) index-based
print(query(1, 3));
# modify element at 2nd index
update_tree_node(2, 1);
# print the sum in range(1,2) index-based
print(query(1, 3));