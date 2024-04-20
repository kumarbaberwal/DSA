import heapq
# queue=[(0,0)]
# print(queue)
# heapq.heappush(queue,(2,1))
# print(queue)
# heapq.heappush(queue,(4,2))
# print(queue)
# heapq.heappush(queue,(3,2))
# print(queue)
# heapq.heappush(queue,(9,3))
# print(queue)
# heapq.heappush(queue,(6,4))
# print(queue)
# heapq.heappush(queue,(8,3))
# print(queue)
# heapq.heappush(queue,(11,5))
# print(queue)
# heapq.heappush(queue,(9,5))
# print(queue)
# queue=[0]
# print(queue)
# heapq.heappush(queue,9)
# print(queue)
# heapq.heappush(queue,3)
# print(queue)
# heapq.heappush(queue,10)
# print(queue)
# heapq.heappush(queue,2)
# print(queue)
# heapq.heappush(queue,6)
# print(queue)
# heapq.heappush(queue,5)
# print(queue)
# heapq.heappush(queue,1)
# print(queue)
# heapq.heappush(queue,8)
# print(queue)

import heapq

# Initial elements
elements = [1, 3, 6, 5, 9, 8, 10, 7, 12]

# Convert the list into a heap
heapq.heapify(elements)
print(elements)

# Output the elements as a min-heap
print("Min-heap:", elements)

# Add another element (2)
heapq.heappush(elements, 2)
print("After adding 2:", elements)

# Remove the smallest element
min_element = heapq.heappop(elements)
print("Smallest element removed:", min_element)
print("Heap after removal:", elements)
