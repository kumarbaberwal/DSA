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
            Current_Node = self.head
            while Current_Node:
                print(Current_Node.data)
                Current_Node = Current_Node.next

    def InsertAtIndex(self, data, index) -> None:
        newNode = Node(data)
        current_node = self.head
        current_index = 0
        while current_node and current_index != index:
            temp = current_node
            current_node = current_node.next
            current_index += 1
        temp.next = newNode
        newNode.next = current_node

    def InsertAtEnd(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = newNode

    def updateNode(self, data, index) -> None:
        current_node = self.head
        position = 0
        if index == position:
            current_node.data = data
            return
        else:
            while position != index and current_node:
                position += 1
                current_node = current_node.next
            if position == index:
                current_node.data = data
                return
            else:
                print('Index is not Present!')
    
    def remove_first_node(self) -> None:
        if self.head is None:
            print('Linked List is Empty!')
            return
        else:
            self.head = self.head.next


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.InsertAtBegining(9)
    linkedlist.InsertAtBegining(10)
    linkedlist.InsertAtBegining(11)
    linkedlist.InsertAtIndex(12, 1)
    linkedlist.InsertAtIndex(13, 1)
    linkedlist.InsertAtEnd(20)
    linkedlist.InsertAtEnd(30)
    linkedlist.updateNode(14, 3)
    # linkedlist.updateNode(14, 9)
    linkedlist.remove_first_node()
    linkedlist.printLL()