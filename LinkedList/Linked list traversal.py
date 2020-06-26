class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = Linked()
    llist.head = Node('Monday')
    second = Node('Tuesday')
    third = Node('Wednesday')
 
    llist.head.next = second;
    second.next = third;
    llist.printList()
  


