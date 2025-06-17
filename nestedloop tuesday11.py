for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print()

for i in range(1,4,1):
    for j in range(1,4):
        print((i,j),end="")
    print()

for i in range(1,11):
    for j in range(1,11):
        print((i*j),end="")
    print()



for i in range(1,5):
    for j in range(1,i+1):
        print('*',end="")

    print()

for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print('#',end="")
    print()


for i in range(1,5,-1):
        print('#',end="")
print()


for i in range(1,5):
    for j in range(1,5):
        print(j,end="")
    print()

for i in range(1,6,2):
    for j in range(1,i+1):
        print(i,end="")
    print()


for i in range(2,9,2):
    for j in range(1,i+1):
        print('#',end="")
    print()


for i in range(2,9,3):
    for k in range(1,3):
        for j in range(1,i+1):
            print('#',end="")

    print()


for i in range(1,5):
    for j in range(i,0,-1):
            print(j,end="")
    print()