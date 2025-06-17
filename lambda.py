s=lambda a,b:a+b
print(s(7,8))


l=[1,2,3,4]
x=lambda l:l[0]
print(x(l))


d={'name':'arun','age':23,'place':'kkd'}
x=lambda d:d['name']
print(x(d))

import math
sqroot=lambda x:math.sqrt(x)
print(sqroot(81))



x=lambda x:len(x)
print(x('hello'))

n=[1,2,3,4]
sq=[]
for i in n:
    sq.append(i**2)
print(sq)

n=[1,2,3,4]
print(list(map(lambda x:x**2,n)))

import math
n=[81,64,25,16]
print(list(map(lambda x:int(math.sqrt(x)),n)))


d=[{'name':'arun','age':23,'place':'kkd'},{'name':'amal','age':21,'place':'ekm'}]
print(list(map(lambda d:d['name'],d)))


colors=['red','green','orange','yellow','blue']
print(list(map(lambda x:len(x),colors)))


l=[['abc','john',300,'english'],['stu','mike',350,'english']]
print(list(map(lambda x:x[1],l)))


n=[12,33,53,67,30]
print(list(filter(lambda x:x%2==0,n)))


colors=['red','green','blue','purple']
print(list(filter(lambda x:len(x)<5,colors)))

print(list(filter(lambda x:x%3==0 and x%5==0,range(1,101))))

n=[12,30,-2,-11,67,-34]
print(list(filter(lambda x:x<0,n)))


print(list(filter(lambda x:'3' in str(x),range(100,200))))


import functools
n=[1,2,3,4]
print(functools.reduce(lambda x,y:x+y,n))