class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.next = None
if __name__=='__main__':
    llist = Linked()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second;
    second.next = third;