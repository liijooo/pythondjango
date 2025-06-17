l=[1,2,3,4,5,6]
new=[]
for i in l:
    new.append(i**2)
    print(new)
print()


l=[45,26,89,12,91,51]
even=[]
odd=[]
for i in l:
    if(i%2==0):
        even.append(i)
        print(even)
    else:
        odd.append(i)
        print(odd)
print()


l=['red',3.4,90,12,6.5,'abc']
alpts=[]
num=[]
flt=[]
count=0
for i in l:
    if(type(i)==str):
        alpts.append(i)
    elif(type(i)==float):
        flt.append(i)
    elif(type(i)==int):
        num.append(i)
    else:
        pass
print("char is",alpts)
print("count is",len(alpts))
print("float is",flt)
print("count",len(flt))
print("numbers",num)
print("count",len(num))


