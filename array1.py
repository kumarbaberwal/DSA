import array as arr 
a=arr.array("i",[1,2,3,4])
print(a)
print()
print(a.buffer_info())
print()
print(a.typecode)
print()
a.append(9)
print()
print(a)
print()
# a.reverse()
# print(a)
print()

for i in range(5):
    print(a[i])