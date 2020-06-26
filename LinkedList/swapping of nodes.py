class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
    def swap(self, x, y):
        if x==y:
            return
        
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    llist = Linked()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    print("Nodes before swapping")
    llist.printList()
    print("Nodes after swapping:")
    llist.swap(3,5)
    llist.printList()
