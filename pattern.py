x="* "
for i in range(5):
    print(f"{x}"*i)

print()

for i in range(5):
    print("* "*i)

print()

y=1
for i in range(5):
    for j in range(1,i+1):
        print(y,end=" ")
        y=y+1
    print()
print()

