class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def insert(temp, key):
    if not temp:
        root = Node(key)
        return

    q= []
    q.append(temp)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

def delete_deepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def delete(root, key):
    if root == None:
        return None

    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root

    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node :
        x =temp.val
        delete_deepest(root, temp)
        key_node.val = x

    return root

def pre_order(root):
    if not root:
        return

    print(root.val, end=" -> ")
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return

    in_order(root.left)
    print(root.val, end=" -> ")
    in_order(root.right)

def post_order(root):
    if not root:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.val, end=" -> ")


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
print("Inorder traversal before insertion:", end = " ")
in_order(root)
print()
key = 12
insert(root, key)
print()
print("Inorder traversal after insertion:", end = " ")
in_order(root)
print()
key = 11
root = delete(root, key)
print()
print("The tree after the deletion;")
in_order(root)
print()