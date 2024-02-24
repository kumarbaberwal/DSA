class Stack:
    def __init__(self) -> None:
        self.stack=[]
        self.top=len(self.stack)-1

    def push(self,item):
        self.stack.append(item)
        self.top=self.top+1

    def pop(self):
        if self.top==-1:
            return "underflow"
        else :
            item=self.stack.pop()
            self.top=self.top-1
            print(item)
    
    def display(self):
        if self.top==-1:
            return "Stack is Empty!"
        else:
            print(self.stack[self.top],">> Top Element")
            # print(self.stack[self.top-1],"Top Element")
            # print(self.stack[self.top-2],"Top Element")
            for i in range(self.top-1,-1,-1):
                print(self.stack[i])


    def is_empty(self):
        if self.top==-1:
            print('True')
        else:
            print('False')


stack=Stack()
stack.push(5)
stack.push(6)
stack.push(9)
stack.display()
print() #for a empty line or next line
stack.pop()
print()
stack.is_empty()
print()
stack.display()