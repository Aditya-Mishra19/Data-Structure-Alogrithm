class Node:
    def __init__(self, data):

        self.data = data
        self.left = self.right = None


# Function to perform inorder traversal of the tree
def inorder(root):

    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


# Iterative function to insert a key into BST.
def insertIterative(root, key):
    curr = root
    parent = None
    if root is None:
        return Node(key)
    while curr:
        parent = curr
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    if key < parent.data:
        parent.left = Node(key)
    else:
        parent.right = Node(key)

    return root



root = None
keys = [15, 10, 20, 8, 12, 16, 25]

for key in keys:
    root = insertIterative(root, key)

inorder(root)
