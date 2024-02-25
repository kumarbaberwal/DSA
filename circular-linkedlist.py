class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.pointer=None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head=None

    def InsertAtStart(self,data):
        newNode=Node(data)
        newNode.pointer=self.head
        if self.head==None:
            self.head=newNode
            newNode.pointer=self.head
            return
        else:
            newNode.pointer=self.head
            self.head=newNode

    # def InsertAtEnd(self,data):


    def display(self):
        pointer=self.head
        print(pointer.data)
        pointer=pointer.pointer
        while pointer!=self.head:
            print(pointer.data)
            pointer=pointer.pointer


circular=CircularLinkedList()
circular.InsertAtStart(4)
circular.InsertAtStart(5)
circular.InsertAtStart(6)
circular.display()