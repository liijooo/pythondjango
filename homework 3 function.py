#function to check palindrome
def palindrome():
    s=input("enter the string")
    rev=""
    for i in s:
        rev=i+rev
    if(s==rev):
        print("palindrome")
    else:
        print("not palindrome")
    print()
palindrome()


#function to check prime
def prime():
    n=int(input("enter the number"))
    if(n>1):
            for i in range(2,n):
                if(n%i==0):
                    print("not prime")
                    break

            else:
                print("prime number")
    else:
        print("not prime")
    print()
prime()

#function to check armstrong
def armstrong():
    n=int(input("enter a number"))
    s=str(n)
    length=len(s)
    total=0
    for i in s:
        total=total+int(i)**length
    if n==total:
        print("armstrong number")
    else:
        print("not a armstrong number")
    print()
armstrong()


#function to print occurences in string
def occurences():
    s=input("enter string")
    letter=input("enter the letter")
    count=0
    for i in s:
        if (i==letter):
            count+=1
    print(letter,"occurs",count,"times")
occurences()
