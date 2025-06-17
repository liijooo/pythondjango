n=int(input("enter a number"))
if(n%2==0):
    if(n%3==0):
        print("divisible by both 2 and 3")
elif(n%2==0):
    if(n%3!=0):
        print("divisible by 2 but not divisible by 3")
elif(n%2!=0):
    if(n%3==0):
        print("not divisible by 2 but divisible by 3")
elif(n%2!=0):
    if(n%3!=0):
        print("both 2 and 3 are not divisible")
else:
    print("error")