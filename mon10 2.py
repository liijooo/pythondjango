n=int(input("enter a number"))
if(n>1):
   for i in range(2,n):
      if n%i==0:
          print(n,"is not a prime number")
          break
   else:
       print(n,"is a prime number")
else:
    print("not a prime number")


l=[1,23]
print(l[-2])

t=(1,'a','banana')

