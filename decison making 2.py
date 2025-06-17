n1=int(input("enter first number"))
n2=int(input("enter second number"))
calc=input("enter the operator:+-*/")
if(calc=='+'):
    print(n1+n2)
elif(calc=='-'):
    print(n1-n2)
elif(calc=='*'):
    print(n1*n2)
elif(calc=='/'):
    print(n1/n2)
else:
    print("invalid")
