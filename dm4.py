l1=['january','march','may','july','august','october','december']
l2=['april','june','september','november']
l3=['february']
month=input("enter the month")
if(month in l1):
    print("there are 31 days")
elif(month in l2):
    print("there are 30 days")
elif(month in l3):
    print("there are 28 days")
else:
    print("error")
