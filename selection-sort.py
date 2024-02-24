# Implementation of Selection sort
a=[8,4,9,2,10,3]
for i in range(len(a)):
    first=i
    for j in range(i+1,len(a)):
        if a[j]<a[first]:
            first=j
    if first!=i:
        a[first],a[i]=a[i],a[first]
print(a)