# Implementation of queue with collections deque

import collections
queue=collections.deque()
queue.append('K')
queue.append('u')
queue.append('m')
queue.append('a')
queue.append('r')
print('Queue after enqueue: ')
print(queue)
print('Elements are dequeue for the queue: ')
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print('Queue after removing elemnts: ')
print(queue)
