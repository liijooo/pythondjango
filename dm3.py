side1=int(input("enter the value"))
side2=int(input("enter the value"))
side3=int(input("enter the value"))
if(side1==side2 and side1==side3 and side2==side3):
    print("equilateral")
elif(side1==side2 and side1!=side3 and side2!=side3):
    print("isosceles")
elif(side1!=side2 and side1!=side3 and side2!=side3):
    print("scalene")
else:
    print("error")