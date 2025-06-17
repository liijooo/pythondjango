n=5
k=4*2 #space initial value
for i in range(1,n+1):
    for p in range(1,k+1): #for printing space
        print(end=" ")
    k=k-2
    for j in range(1,i+1):  #for printing star
        print('*',end="   ")
    print()
k=2
for i in range(4,0,-1):
    for p in range(1,k+1):
        print(" ",end="")
    k=k+2
    for j in range(1,i+1):
        print('*',end="   ")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        if j%2!=0:
            print(1,end=" ")
        else:
            print('A',end=" ")
    print()