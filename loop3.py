i=200
while(i<=500):
    if (i%3==0 and i%5==0):
        print(i,end=" ")
    i=i+1
print()

i=1
while(i<=100):
    if(i%7==0):
        print(i,end=" ")
    i=i+1
print()

i=1
count=0
while(i<=100):
    if(i%3==0):
        count+=1
    i=i+1
print("count is",count)
print()


i=1500
count=0
while(i<=2700):
    if(i%5==0 and i%7==0):
        count+=1
    i=i+1
print("count of numbers divisible by 5 and 7 is",count)
print()

sum=0
i=1
while(i<=10):
    sum=sum+i
    print(sum,end=" ")
    i=i+1
print()

sum=0
i=200
while(i<=400):
    sum=sum+i
    print(sum,end=" ")
    i=i+1
print()

sum=0
i=1
while(i<=10):
    sum=sum+i**2
    print(sum,end=" ")
    i=i+1
print()

sum=0
i=2
while(i<=100):
    sum=sum+i
    print(sum,end=" ")
    i=i+2
print()


i=1
count=0
sum=0
while(i<=50):
    if(i%3==0):
        count+=1
        sum=sum+i
    i=i+1
print(sum)
print("count is",count)
print()

i=1
prod=1
while(i<=10):
    prod=prod*i
    print(prod)
    i=i+1
print()


n=int(input("enter number"))
i=1
prod=1
while(i<=n):
    prod=prod*i
    print("factorial",prod)
    i=i+1


n=int(input("enter number"))
i=1
while(i<=n):
    if(n%i==0):
        print("factors",i)
    i=i+1