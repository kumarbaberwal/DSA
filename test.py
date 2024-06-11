class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data) -> None:
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def prepend(self, data) -> None:
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        else:
            newNode.next = self.head
            self.head.previous = newNode
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

            if current_index != index - 1:
                print('Index not Found')
                return
            newNode.next = current_node.next
            current_node.next = newNode

    def updateNode(self, data , index) -> None:
        current_index = 0
        current_node = self.head
        if index < 0 :
            print('Invalid Index')
            return
        else:
            if current_index == index:
                self.head.data = data
                return
            else:
                while current_index < index - 1 and current_node.next != self.head:
                    current_index += 1
                    current_node = current_node.next
                if current_index != index - 1:
                    print('Index is not Present')
                    return
                current_node.next.data = data

    def remove_first_node(self) -> None:
        if not self.head:
            print('Circular Linked List is Empty!')
            return
        elif self.head == self.head.next:
            self.head = None
            return
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            self.head = self.head.next
            last_node.next = self.head

    def remove_last_node(self) -> None:
        if not self.head:
            print('Circular Linked List is Empty')
            return
        elif self.head.next == self.head:
            self.head = None
            return
        else:
            last_node = self.head
            while last_node.next.next != self.head:
                last_node = last_node.next
            last_node.next = self.head

    def remove_at_index(self, index) -> None:
        current_index = 0
        if not self.head:
            print('Circular Linked List is Empty!')
            return
        elif current_index == index:
            if self.head.next == self.head:
                self.head = None
                return
            else:
                self.remove_first_node()
        else:
            current_node = self.head
            previous_node = None
            while current_node.next != self.head and current_index < index:
                previous_node = current_node
                current_node = current_node.next
                current_index += 1
            if current_index != index:
                print("Index is not Present")
                return
            previous_node.next= current_node.next

    def sizeOfCLL(self) -> None:
        if not self.head:
            print('Circular Linked List is Empty')
            return
        else:
            current_index = 0
            current_node = self.head
            while current_node.next != self.head:
                current_index += 1
                current_node = current_node.next

            print(f'The size of circular linked list is {current_index + 1}')

    def printCLL(self) -> None:
        if not self.head:
            print('Doubly Linked List is Empty')
            return
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def printRCLL(self) -> None:
        if not self.head:
            print('Doubly Linked List is Empty')
            return
        else:
            current_node = self.tail
            while current_node:
                print(current_node.data)
                current_node = current_node.previous

if __name__ == '__main__':
    doublyLL = DoublyLinkedList()
    # doublyLL.printCLL()
    doublyLL.append(1)
    doublyLL.append(2)
    doublyLL.append(3)
    doublyLL.append(4)
    doublyLL.append(5)
    doublyLL.prepend(6)
    # doublyLL.insertAtIndex(19, 3)
    # doublyLL.updateNode(20, 3)
    # doublyLL.remove_first_node()
    # doublyLL.remove_last_node()
    # doublyLL.remove_at_index(2)
    # doublyLL.sizeOfCLL()
    doublyLL.printCLL()
    print()
    doublyLL.printRCLL()