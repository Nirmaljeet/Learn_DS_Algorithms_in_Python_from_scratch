class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ =='__main__':
    llist = Linked()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    print('Linked List before reversing is:', llist.printList())
    llist.reverse()
    print('Linked List after reversal is: ', llist.printList())
