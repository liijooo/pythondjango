import math
n=[81,9,25,16,64]
print(list(map(lambda x:x**0.5,n)))

n=[81,9,25,16,64]
for i in n:
    for j in range(1,i+1):
        if j*j==i:
            print(i,j)
            break


from areaop import circle
circle(3,6)








