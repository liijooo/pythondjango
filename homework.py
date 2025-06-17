#check whether a number is prime or not
n=int(input("enter a number"))
if(n<=1):
   for i in range(2,n):
       if(n%i==0):
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
else:
    print("not prime number")
print()

#check whether a number is armstrong number or not
n=int(input("enter a number"))
s=str(n)
length=len(s)
sum=0
for i in s:
    sum=sum+int(i)**length
if(n==sum):
    print("armstrong number")
else:
    print("not a armstrong number")



#check whether the number is palindrome or not
#n=int(input("enter a number"))
#original=n
#rev_num=0
#while(n>0):
 #   rev_num=rev_num*10+n%10
  #  n//=10
#if original==rev_num:
 #   print(original,"is a palindrome number")
#else:
 #   print(original,"is not a palindrome number")
#print()

#count the occurence of each character in string
#s="hello"
#count={}
#for i in s:
 #   if i in count:
  #      count[i]+=1
  #  else:
   #     count[i]=1
#for i,j in count.items():
 #   print(i,j)