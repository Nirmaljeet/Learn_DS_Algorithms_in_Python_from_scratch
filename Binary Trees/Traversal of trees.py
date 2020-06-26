class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)


root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)



print('Preorder traversal is: ')
printPreorder(root)
