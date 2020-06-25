class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, key):
        temp = self.head
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None

    def Print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
if __name__ =='__main__':
    llist = Linked()
    llist.head = Node(7)
    second = Node(2)
    third = Node(3)
    new_data = Node(4)
    llist.head.next = second;
    second.next = third;
    third.next = new_data;
    llist.push(5)
    llist.push(6)
    print('Linked List before deletion')
    llist.Print()
    print('Linked list after deletion')
    llist.delete(2)
    llist.Print()
