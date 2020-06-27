class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data

def inorder(temp):
    if(not temp):
        return

    inorder(temp.left)
    print(temp.key, end = "")
    inorder(temp.right)

def insert(temp, key):
    q = []
    q.append(temp)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if(not temp.left):
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print('Before insertion: ')
inorder(root)

key = 8
insert(root, key)
print()
print('After Insertion')
inorder(root)