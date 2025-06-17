from socketserver import ThreadingTCPServer

n=int(input("enter number"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()

# aptitude
#
# two third distance=2/3*6=4km
# time=distance/speed=4/4=1hr
# remaining distance=6-4=2km
# time=24/60=2/5hrs
# speed=distance/time=2/2/5=2*5/2
# answer=5km/hr