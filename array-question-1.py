arr=[4,7,2,9,6]
arr2=[1,2,9,3,4]
max=arr[0]
for i in range(len(arr2)-1):
    if max<arr2[i]:
        max=arr2[i]
        index=i
count=0
for i in range(len(arr2)-1):
    if i==index:
        continue
    else:
        if arr2[i]**2>max:
            count+=1
if count!=0:
    print('-1')
else:
    print(index)