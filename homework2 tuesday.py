l=['kelly','jenny','emi']
for i in l:
    for j in range(1,4):
        print(i,end=" ")
    print()

serial_no=[1,2,3]
qns=['what','why','when']
for i in serial_no:
    print(i)
    for j in qns:
        print(j)
    print()

d={1:['lion','tiger','horse'],2:['cat','dog','cow']}
for i in d.values():
    for j in i:
        print(j)

num=1
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        num=num+1
    print()


for i in range(1,5):
    for j in range(i):
        print(i*i,end=" ")
    print()
