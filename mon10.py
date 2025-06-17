n=123
s=('123')
for i in s:
    print(i)

n=123
while(n>0):
    n1=n%10
    print(n1)
    n=n//10

n=123
s='123'
sum=0
for i in s:
    sum=sum+int(i)
    print(sum)

s=input("enter the string")
ch=input("enter the character")
count=0
for i in s:
    if(i==ch):
        count=count+1
print(count)

s="hello"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
    print(d)
print(d)


for i in range(1,10):
    print(i)
    if(i==3):
        break
else:
    print("hello")