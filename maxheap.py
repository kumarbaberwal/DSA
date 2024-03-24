arr=[3,9,2,4,10,1,5,6,11]

def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right

    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)


n=len(arr)
for i in range((n//2)-1,-1,-1):
    heapify(arr,n,i)


print(arr)