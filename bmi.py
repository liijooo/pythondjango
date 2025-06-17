height=int(input("enter the height in cm:"))
weight=int(input("enter the weight in kg:"))
height_in_m=height/100
bmi=weight/height_in_m**2
if(bmi<18.5):
    print("underweight")
elif(18.5-24.9):
    print("normal")
elif(25-29.9):
    print("overweight")
elif("obesity"):
    if(30-34.9):
        print("mild")
    elif(35-39.9):
        print("moderate")
    elif(bmi<40):
        print("morbid")
else:
    print("error")