def add(a,b):
    sum=a+b
    print(sum)
n1=int(input("enter first number"))
n2=int(input("enter second number"))
add(n1,n2)


def add():
    a=int(input("enter number"))
    b=int(input("enter number"))
    sum=a+b
    return sum
s=add()
print(s)


def add(a,b):
    sum=a+b
    return sum

n1=int(input("enter number"))
n2=int(input("enter number"))
s=add(n1,n2)
print(s)


def simple_interest(p,n,r):
    si=p*n*r/100
    return si
n1=int(input("enter amount"))
n2=int(input("enter years"))
n3=int(input("enter rate"))
s=simple_interest(n1,n2,n3)
print(s)


def sum():
    a=int(input("enter number"))
    b=int(input("enter number"))
    add=a+b
    sub=a-b
    prod=a*b
    div=a/b
    return add,sub,prod,div

s=sum()
print(s)