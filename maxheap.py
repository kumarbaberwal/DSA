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


for i in range((len(arr)//2)-1,-1,-1):
    heapify(arr,len(arr),i)


print(arr)
def insert(arr,n,val):
    arr.append(val)
    i=n
    while i>0:
        parent=(i-1)//2
        if arr[parent]<arr[i]:
            arr[parent],arr[i]=arr[i],arr[parent]
            i=parent
        else:
            return
insert(arr,len(arr),7)
print(arr)
insert(arr,len(arr),20)

print(arr)