a=[8,4,9,2,0,10,3,1.6]
sort=a[0]
for i in range(len(a)):
    if sort>a[i]:
        sort=a[i]
print(sort)