class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def ancestors(root, target):
    if root == None:
        return False

    if root.data==target:
        return True

    if (ancestors(root.left, target) or 
        ancestors(root.right, target)): 
        print(root.data)
        return True

   

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

print(ancestors(root, 5))
