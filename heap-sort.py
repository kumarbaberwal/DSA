arr=[12,11,5,6,7,1,3]
def heapify(arr,n,i):
    largest=i
    l=(2*i)+1
    r=(2*i)+2

    if l<n and arr[l]>arr[largest]:
        largest=l

    if r<n and arr[r]>arr[largest]:
        largest=r

    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)


def heapsort(arr):
    n=len(arr)-1
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

heapsort(arr)
print(arr)