arr=[-3,-4,7,9,3,9,4]
arr.sort()
count=0
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        count+=1
print(count)