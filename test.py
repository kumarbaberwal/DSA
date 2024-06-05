class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            return
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = newNode
            newNode.next = self.head

    def prepend(self, data) -> None:
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.head.next = self.head
            return
        else:
            newNode.next = self.head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = newNode
            self.head = newNode

    def insertAtIndex(self, data, index) -> None:
        newNode = Node(data)
        current_index = 0
        if current_index == index:
            self.append(data)
        else:
            current_node = self.head
            while current_index < index - 1 and current_node.next != self.head:
                current_index += 1
                current_node = current_node.next

            if current_index != index:
                print('Index not Found')
                return
            newNode.next = current_node.next
            current_node.next = newNode

    def printCLL(self) -> None:
        if self.head is None:
            print('Circular Linked List is Empty!')
            return
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next
                if current_node == self.head:
                    break

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.printCLL()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(4)
    linkedlist.append(5)
    linkedlist.prepend(6)
    linkedlist.insertAtIndex(19, 3)
    linkedlist.printCLL()