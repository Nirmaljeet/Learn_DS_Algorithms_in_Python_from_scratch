class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printKDistant(root, k):
    if root is None:
        return

    if k == 0:
        print (root.data)

    else:
        printKDistant(root.left, k-1)
        printKDistant(root.right, k-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

printKDistant(root, 2)