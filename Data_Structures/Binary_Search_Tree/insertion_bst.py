# define a binary search tree node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# define a function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)                