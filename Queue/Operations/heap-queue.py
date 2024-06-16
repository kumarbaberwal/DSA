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
