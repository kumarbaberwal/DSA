class Queue:
    def __init__(self, size) -> None:
        self.queue = []
        self.front = self.rear = 0
        self.size = size

    def enqueue(self, item) -> None:
        if self.size == self.rear:
            print('Queue is Full')
        else:
            self.queue.append(item)
            self.rear += 1

    def dequeue(self) -> None:
        if self.front == self.rear:
            print('Queue is Empty')
        else:
            self.rear -= 1
            return self.queue.pop(0)
    
    def display(self) -> None:
        if self.front == self.rear:
            print('Queue is Empty')
        else:
            for i in self.queue:
                print(i , '<--')

    def isEmpty(self) -> str:
        if self.front == self.rear: print('True')
        else: print('False')


if __name__ == '__main__':
    queue = Queue(3)
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    queue.display()
    queue.isEmpty()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    queue.isEmpty()