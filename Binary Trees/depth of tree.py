class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def maxDepth(node):
    if node is None:
        return 0 ;

    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth +1
        else:
            return rDepth + 1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(6)

print('Max depth is: ', maxDepth(root))