class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        self.hd = 0

def topView(root):
    if(root == None):
        return

    q = []
    m = dict()
    hd = 0
    root.hd = hd

    q.append(root)
    while(len(q)):
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd] = root.data

        if (root.left):
            root.left.hd = hd - 1
            q.append(root.left)

        if (root.right):
            root.right.hd = hd + 1
            q.append(root.right)

            q.pop(0)

    for i in sorted(m):
        print(m[i])

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(4)
root.right.right = Node(5)
print('Top view of tree is: ')
topView(root)