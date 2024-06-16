# stack implementation using deque

import collections

stack=collections.deque()
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print("Initial Stack: ")
print(stack)
print()
print("Popping Elements from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print()
print("Stack after Popping Elements: ")
print(stack)
