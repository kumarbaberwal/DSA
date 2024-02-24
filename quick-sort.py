# Implementation of quick sort 
a=[8,4,9,2,10,3,0,10,1,12]
def partition(a,start,end):
    lb=start
    ub=end
    first=a[lb]
    while (lb<ub):
        while (a[lb]<=first):
            lb=lb+1
        while (a[ub]>first):
            ub=ub-1
        if (lb<ub):
            a[lb],a[ub]=a[ub],a[lb]
    a[start],a[ub]=a[ub],a[start]
    return ub
def quicksort(a,start,end):
    if start<end:
        index=partition(a,start,end)
        quicksort(a,start,index-1)
        quicksort(a,index+1,end)
quicksort(a,0,len(a)-1)
print(a)