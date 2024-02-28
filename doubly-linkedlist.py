class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.previous=None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None

    def InsertAtBegining(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode

    def display(self):
        pointer=self.head
        while pointer:
            print(pointer.data)
            pointer=pointer.next


doublelist=DoublyLinkedList()
doublelist.InsertAtBegining(1)
doublelist.InsertAtBegining(2)
doublelist.InsertAtBegining(3)
doublelist.InsertAtBegining(4)
doublelist.InsertAtBegining(5)

doublelist.display()