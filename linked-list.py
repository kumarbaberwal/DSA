class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.pointer=None


class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def InsertAtBegining(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            newNode.pointer=self.head
            self.head=newNode

    def display(self):
        pointer=self.head
        while pointer:
            print(pointer.data)
            pointer=pointer.pointer


linkedlist=LinkedList()

linkedlist.InsertAtBegining(5)
linkedlist.InsertAtBegining(9)
linkedlist.display()