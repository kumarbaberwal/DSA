arr=[8,1,9,2,4,3,5,7,6]

def partition(arr,start,end):
    i=start
    j=end
    pivot=arr[start]
    while (i<j):
        while arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[start],arr[j]=arr[j],arr[start]
    return j

def quicksort(arr,start,end):
    if start<end:
        index=partition(arr,start,end)
        quicksort(arr,start,index-1)
        quicksort(arr,index+1,end)

quicksort(arr,0,len(arr)-1)

print(arr)