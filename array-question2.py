arr=[-3,-4,7,9,3,9,4]
arr.sort()
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            count+=1
            break
print(count)