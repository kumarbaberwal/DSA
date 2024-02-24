# Implementation of queue using queue

import queue
q=queue.Queue(maxsize=5)
print(q.qsize())
q.put('K')
q.put('u')
q.put('m')
q.put('a')
q.put('r')
# q.put('B') #it terminates the program and stuck it between 
print(q.qsize())
print('Checking Full: ',q.full())
print('Elemetns dequeue from the queue: ')
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get()) #it also stuck the program in between 
print('Queue after removing elements: ')
print(q)