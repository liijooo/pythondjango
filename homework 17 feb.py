n=int(input("enter number"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()

s="hello"
l=len(s)
for i in range(0,l,2):
    print(s[i],end="")
