km=int(input("enter the km"))
if(km<=5):
  print("fare is:",10*km)
elif(km>=6 and km<=15):
   print("Fare is:",8*km)
elif(km>=16 and km<=30):
   print("fare is:",6*km)
elif(km>=30):
   print("fare is:",5*km)
else:
   print("wrong input")


print(1,"For battery based toys")
print(2,"For key based toys")
print(3,"For Charging based toys")
prod_code=int(input("enter the code(1,2,3):"))
price=int(input("enter the price:"))
if(prod_code==1):
    if(price>=1000):
        discount_price=price*0.1
        actualprice=price-discount_price
    else:
        actualprice=price
elif(prod_code==2):
    if(price>100):
        discount_price=price*0.05
        actualprice=price-discount_price
    else:
        actualprice=price
elif(prod_code==3):
    if(price>500):
        discount_price=price*0.05
        actualprice=price-discount_price
    else:
        actualprice=price
else:
    print("not applicable")
