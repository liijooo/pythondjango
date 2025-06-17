#sum of elements in list
l=[11,23,67,34]
sum=0
for i in l:
    sum=sum+i
print("sum is",sum)
print()

#reverse of given string
s="hello"
rev=""
for i in s:
    rev=i+rev
print("reversed string is",rev)
print()


#remove duplicates
s="programming"
new=" "
for i in s:
    if(i not in new):
        new+=i
    print(new)
print()

d={101:['arun',20,'ekm'],102:['amal',26,'tvm'],103:['anu',29,'tvm']}
for i in d.values():
    print(i[0])
print()

colors=['red','green','orange','purple','black','blue']
new=[]
for i in colors:
    if(i[0]=='b'):
        new.append(i)
    print(new)

