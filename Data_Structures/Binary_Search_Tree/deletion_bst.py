#define a node of a binary search tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

'''
Note: This is not a generic inorder successor
function. It mainly works when the right child is not empty,
which is the case we need in BST delete.
'''

def get_successor(current): # define a function to get the inorder successor which takes the current node as input
    current = current.right # go to the right child of the current node
    while current is not None and current.left is not None: # while the current node is not None and the left child of the current node is not None we go to the left child of the current node
        current = current.left # go to the left child of the current node
    return current # finally return the current node which is the inorder successor of the node to be deleted

# define a function that deletes a given key x from the given BST and returns the modified root of the BST
def delete_node(root, key):
    # Here we will use recursion to delete the node
    
    # base case: if the root is None, return None
    if root is None:
        return root
    
    # recursive case: if the key is less than the root's key, go to the left subtree
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # If the root matches with the given key
        # Case 1: if the node has no child (leaf node)
        if root.left is None:
            return root.right
        # Case 2: if the node has only left child
        if root.right is None:
            return root.left
        # Case 3: if the node has both children
        # get the inorder successor (smallest in the right subtree)
        successor = get_successor(root)
        # copy the inorder successor's value to this node
        root.key = successor.key
        # delete the inorder successor
        root.right = delete_node(root.right, successor.key)
    return root # finally return the root of the modified BST

# define a function to do inorder traversal of the BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# Driver code
if __name__ == "__main__":
    # create the root node
    root = Node(50)
    # insert nodes into the BST
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    print("Inorder traversal of the given tree:")
    inorder(root) # print the inorder traversal of the BST
    print()

    # delete a node with key 20
    print("\nDelete 20:")
    root = delete_node(root, 20)
    inorder(root) # print the inorder traversal of the modified BST
    print()

    # delete a node with key 30
    print("\nDelete 30:")
    root = delete_node(root, 30)
    inorder(root) # print the inorder traversal of the modified BST
    print()

    # delete a node with key 50
    print("\nDelete 50:")
    root = delete_node(root, 50)
    inorder(root) # print the inorder traversal of the modified BST