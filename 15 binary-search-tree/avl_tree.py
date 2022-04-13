class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:
    def insert(self, root,key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, some_node):
        some_node_right = some_node.right
        some_node_right_left = some_node_right.left

        some_node_right.left = some_node
        some_node.right = some_node_right_left

        some_node.height = 1 + max(self.get_height(some_node.left), self.get_height(some_node.right))
        some_node_right.height = 1 + max(self.get_height(some_node_right.left), self.get_height(some_node_right.right))

        return some_node_right

    def right_rotate(self, some_node):
        some_node_left = some_node.left
        some_node_left_right = some_node_left.right

        some_node_left.right = some_node
        some_node.left = some_node_left_right

        some_node.height = 1 + max(self.get_height(some_node.left), self.get_height(some_node.right))
        some_node_left.height = 1 + max(self.get_height(some_node_left.left), self.get_height(some_node_left.right))

        return some_node_left

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

    def pre_order(self, root):
        if not root:
            return

        print(f"{root.val} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

my_tree = AVL_Tree()
root = None

root = my_tree.insert(root, 10)
root = my_tree.insert(root, 20)
root = my_tree.insert(root, 30)
root = my_tree.insert(root, 40)
root = my_tree.insert(root, 50)
root = my_tree.insert(root, 25)

print("Preorder traversal of the constructed AVL tree is")
my_tree.pre_order(root)
print()

my_tree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = my_tree.insert(root, num)

# Preorder Traversal
print("Preorder Traversal after insertion -")
my_tree.pre_order(root)
print()

# Delete
key = 10
root = my_tree.delete(root, key)

# Preorder Traversal
print("Preorder Traversal after deletion -")
my_tree.pre_order(root)
print()