#1.print series
for i in range(3,31,3):
    print(i,end=" ")
print()


for i in range(1,5):
    for j in range(1,i+1):
        print(2,end=" ")
    print()

s="python"
n=len(s)
for i in range(1,n+1):
    print(s[:i])
print()

#fruits
fruits=['orange','banana','apple','pineapple','avocado']
for i in fruits:
    if i[0]=='a':
        print(i)
        break
    print()

for i in range(1,50):
    print(i,'-',50-i)
print()


#spy number
n=input("enter number")
sum=0
product=1
for i in n:
    d=int(i)
    sum+=d
    product*=d
if sum==product:
    print("spy number")
else:
    print("not spy number")