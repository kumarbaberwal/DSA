a=[]
b=int(input('Enter the lenght of array: '))
for i in range(b):
    y=int(input('Enter the element of array: '))
    a.append(y)
a.sort()
print('Array after sort is : ')
for i in range (len(a)):
    print(a[i])

x=int(input('Enter the Number you want to search: '))
start=0
end=len(a)
mid=int((start+end)/2)
while start<end and x!=a[mid]:
    if x>a[mid]:
        start=mid+1
    else:
        end=mid-1
    mid=int((start+end)/2)

if x==a[mid]:
    print('Element found at ',mid,' in the array.')
else:
    print('Match Not Found!')