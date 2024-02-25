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

    def InsertAtIndex(self,data,index):
        newNode=Node(data)
        pointer=self.head
        i=0
        while i<index:
            temp=pointer
            pointer=pointer.pointer
            i=i+1
        temp.pointer=newNode
        newNode.pointer=pointer

    def InsertAtEnd(self,data):
        newNode=Node(data)
        pointer=self.head
        while pointer:
            temp=pointer
            pointer=pointer.pointer
        temp.pointer=newNode



linkedlist=LinkedList()

linkedlist.InsertAtBegining(5)
linkedlist.InsertAtBegining(9)
linkedlist.InsertAtBegining(10)
linkedlist.InsertAtIndex(13,1)
linkedlist.InsertAtEnd(40)
linkedlist.display()