n=int(input("enter a number"))
if(n%15==0):
    print("pingpong")
elif(n%5==0):
    print("pong")
elif(n%3==0):
    print("ping")
else:
    print("error")