num_cars=int(input("enter number of cars"))
cars=[]
for i in range(num_cars):
    print(i+1,"car details")
    brand=input("brand:")
    model=input("model:")
    km=int(input("total km:"))
    mileage=int(input("mileage"))
    cars.append({"brand":brand,"model":model,"km":km,"mileage":mileage})
unique_brands=[]
for car in cars:
    if car["brand"] not in unique_brands:
        unique_brands.append(car["brand"])
print("unique car brands",unique_brands)
print("car details")
for car in cars:
    print(car)

fuel_usage=[]
for car in cars:
    fuel_used=car["km"]/car["mileage"]
    fuel_usage.append((car["model"],fuel_used))

for i in range(len(fuel_usage)-1):
    for j in range(i+1,len(fuel_usage)):
        if fuel_usage[i][1]>fuel_usage[j][1]:
            fuel_usage[i],fuel_usage[j]=fuel_usage[j],fuel_usage[i]

print("fuel used sorted by efficiency")
for model,fuel in fuel_usage:
    print(model,":",fuel,"L")

least_efficient_car=fuel_usage[-1]
print("least efficient car",least_efficient_car[0],",",least_efficient_car[1],"L")



# aptitude
# =1/15+1/20
#    4/60+3/60=7/60
#       4*7/60=28/60=7/15
#           1-7/15=8/15
#
# answer=8/10

