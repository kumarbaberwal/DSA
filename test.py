class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.pointer=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def InsertAtEnd(self,data):
        NewNode=Node(data)
        if self.head is None:
            self.head=NewNode
            return
        else:
            pointer=self.head
            while pointer:
                temp=pointer
                pointer=pointer.pointer
            temp.pointer=NewNode
    def display(self):
        pointer=self.head
        while pointer:
            print(pointer.data)
            pointer=pointer.pointer

    def InsertAtStart(self,data):
        NewNode=Node(data)
        if self.head==None:
            self.head=NewNode
            return
        else:
            NewNode.pointer=self.head
            self.head=NewNode

linklist=LinkedList()
linklist.InsertAtEnd(4)
linklist.InsertAtEnd(5)
linklist.InsertAtEnd(6)
linklist.InsertAtEnd(7)

# linklist.display()

linklist.InsertAtStart(1)
linklist.InsertAtStart(2)
linklist.InsertAtStart(3)
linklist.display()