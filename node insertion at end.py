class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    
    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = Linked()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    new_node = Node(4)
    llist.head.next = second;
    second.next = third;
    third.next = new_node; 
    llist.PrintList()