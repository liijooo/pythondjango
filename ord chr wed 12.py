n=65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n=n+1
    print()


n=65
for i in range(1,5):
    for j in range(i):
        print(chr(n),end=" ")
        n=n+1
    print()


