a=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    x=input("Enter the element : ")
    a.append(x)
    
print("The array is: ")
print()
for i in range(n):
    print(a[i])

b=input("Enter the element you want to search: ")

print()
print(type(b))
print()
print(type(a))
print()
c=0
# print(len(a))
# print()
# print(range(len(a)))
for i in range (len(a)):
    if a[i]==b:
        c+=1
if c!=0:
    print("Match Found!")
else:
    print("Match Not Found")
# if b in a:
#     print("Match Found!")
# else:
#     print("Match Not Found!")

print()    
print(type(a[3]))
print()