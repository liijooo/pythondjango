n=[23,45,67,12,80,34]
for i in n:
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,"prime number")


for i in range(1,101):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)