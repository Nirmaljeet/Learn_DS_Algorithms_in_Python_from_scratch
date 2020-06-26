class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
    
    def InsertAfter(self, prevNode, new_data):
        if second is None:
            print("The previous node has to be in LinkedList")
            return
        new_node = Node(new_data)
        new_data.next = second.next
        second.next = new_data

    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = Linked()
    llist.head = Node(1)
    new_node = Node(4)
    second = Node(2)
    third = Node(3)
    llist.head.next = new_node;
    new_node.next = second;
    second.next = third;


    
    llist.PrintList()