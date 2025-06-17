n=int(input("enter a number"))
for i in range(n):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
                print("prime number")


n=int(input("enter number"))
for i in range(1,11):
    print(n,'*',i,n*i)


n=int(input("enter number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)



s='hello'
vowels='aeiou'
count=0
for i in s:
    if i in vowels:
        count+=1
print(count)





