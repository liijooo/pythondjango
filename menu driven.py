def sum(n1,n2):
    sum=n1+n2
def sub(n1,n2):
    sub=n1-n2
def prod(n1,n2):
    prod=n1*n2
def div(n1,n2):
    div=n1/n2
def menu() :
    while(1):
        print("arithmetic operations")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.exit")
        ch=int(input("enter your choice"))
        if ch in [1,2,3,4]:
            n1=int(input("enter number"))
            n2=int(input("enter number"))
            if(ch==1):
                sum(n1,n2)
            elif(ch==2):
        sub(n1,n2)
    elif(ch==3):
        prod(n1,n2)
    elif(ch==4):
        div(n1,n2)
    else:
        exit()

sum()
sub()
prod()
div()