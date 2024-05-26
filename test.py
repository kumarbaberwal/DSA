class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def InsertAtBegining(self, data) -> None:
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        else:
            NewNode.next = self.head
            self.head = NewNode

    def printLL(self) -> None:
        if self.head is None:
            print('Linked List is Empty!')
            return
        else:
            curr_none = self.head
            while curr_none:
                print(curr_none.data)
                curr_none = curr_none.next

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.InsertAtBegining(9)
    linkedlist.InsertAtBegining(10)
    linkedlist.InsertAtBegining(11)
    linkedlist.printLL()