# Implementation of insertion sort
a=[8,4,9,2,10,3,0,10,1,12]
for i in range(len(a)):
    first=a[i]
    j=i-1
    while j>=0 and first<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=first
print(a)