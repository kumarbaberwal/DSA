class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.pointer=None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head=None

    def InsertAtBegin(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            newNode.pointer=self.head
            return

        else:
            pointer=self.head.pointer
            while pointer!=self.head:
                temp=pointer
                pointer=pointer.pointer
            newNode.pointer=self.head
            self.head=newNode
            temp.pointer=self.head

    def InsertAtEnd(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            newNode.pointer=self.head
            return
        
        else:
            pointer=self.head
            if pointer.pointer==self.head:
                pointer.pointer=newNode
                newNode.pointer=self.head
                return
            
            else:
                pointer=self.head.pointer
                while pointer!=self.head:
                    temp=pointer
                    pointer=pointer.pointer
                temp.pointer=newNode
                newNode.pointer=self.head

    def display(self):
        pointer=self.head.pointer
        print(self.head.data)
        while pointer!=self.head:
            print(pointer.data)
            pointer=pointer.pointer



circular=CircularLinkedList()
circular.InsertAtEnd(4)
circular.InsertAtEnd(5)
circular.InsertAtEnd(6)

circular.InsertAtBegin(1)
circular.InsertAtBegin(2)

circular.display()