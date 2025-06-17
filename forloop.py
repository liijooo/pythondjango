for i in range(1,6):
    print("hello")
print()

for i in range(1,101):
    print(i)
print()

for i in range(1,11,2):
    print(i)
print()

for i in range(2,11,2):
    print(i)
print()

for i in range(10,91,10):
    print(i)
print()

for i in range(1,11):
    print(i**2)
print()

for i in range(1,40,5):
    print(i)
print()

for i in range(5,0,-1):
    print(i)
print()

for i in range(8,-1,-2):
    print(i)
print()

sum=0
for i in range(1,11):
    sum=sum+i**3
print(sum)
print()

n=int(input("enter number"))
prod=1
for i in range(1,n+1):
    prod=prod*i
print(prod,end=" ")
print()

n=int(input("enter number"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)
print()

for i in range(200,501):
    if(i%3==0 and i%5==0):
        print(i)
