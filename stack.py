class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = len(self.stack) - 1
    
    def push(self, item) -> None:
        self.stack.append(item)
        self.top += 1
    def pop(self) -> None:
        if self.top == -1:
            return "UnderFlow!!!"
        else:
            self.top -= 1
            return self.stack.pop()
        
    def display(self) -> None:
        if self.top == -1:
            print('Stack is Empty.')
        else: 
            print(self.stack[self.top], '>>> Top Element')
            for i in range(self.top-1, -1, -1):
                print(self.stack[i])

    def isEmpty(self) -> str:
        if self.top == -1: return True
        else: return False
    

if __name__ == "__main__":
    stack = Stack()
    stack.push(8)
    stack.push(9)
    stack.push(10)
    stack.push(2)
    stack.push(5)
    stack.display()
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.display()
    print(stack.isEmpty())