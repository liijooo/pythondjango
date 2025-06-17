n=int(input("enter a number"))
if(10<=n<=99):
    print("it is a two digit number")
elif(100<=n<=999):
    print("it is a three digit number")
elif(1000<=n<=9999):
    print("it is a four digit number")
else:
    print("it is either single digit or more than four digit number")