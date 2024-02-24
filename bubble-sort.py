# Implementation of bubble sort 
a=[8,4,9,2,10,3]
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if (a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)