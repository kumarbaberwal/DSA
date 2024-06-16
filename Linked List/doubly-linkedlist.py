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
            self.prepend(data)
            return
        else:
            current_node = self.head
            while current_index < index and current_node:
                previous_node = current_node
                current_node = current_node.next
                current_index += 1
            if current_index != index:
                print("Given Index Not Found!")
                return
            if not current_node:
                self.append(data)
                return
            newNode.next = current_node
            newNode.previous = previous_node
            previous_node.next = newNode
            current_node.previous = newNode

    def updateNode(self, data , index) -> None:
        current_index = 0
        if current_index == index:
            self.head.data = data
            return
        else:
            current_node = self.head
            while current_index < index and current_node:
                current_node = current_node.next
                current_index += 1
            if current_index != index:
                print('Index is not Present in the linked list')
                return
            current_node.data = data

    def remove_first_node(self) -> None:
        if not self.head:
            print('Doubly Linked list is Empty')
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def remove_last_node(self) -> None:
        if not self.head:
            print('Doubly Linked List is Empty!')
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

    def remove_at_index(self, index) -> None:
        if not self.head:
            print('Doubly Linked List is Empty!')
            return
        
        current_node = self.head
        current_index = 0
        if index == 0 and current_node:
            self.head = current_node.next
            if self.head:
                self.head.previous = None
            if current_node == self.tail:
                self.tail = None
            return
        else:
            while current_index < index and current_node:
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
        if current_node:
            previous_node.next = current_node.next
            if current_node.next:
                current_node.next.previous = previous_node
            if current_node == self.tail:
                self.tail = previous_node
        else:
            print('Index not present')
                 
    def sizeOfDLL(self) -> None:
        if not self.head:
            print('Doubly Linked List is Empty!')
            return
        else:
            size = 0
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            
            print(f'The Size of Doubly Linked list is {size}')

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
    doublyLL.insertAtIndex(19, 3)
    doublyLL.updateNode(20, 6)
    doublyLL.remove_first_node()
    doublyLL.remove_last_node()
    doublyLL.remove_at_index(2)
    doublyLL.sizeOfDLL()
    doublyLL.printCLL()
    # print()
    # doublyLL.printRCLL()