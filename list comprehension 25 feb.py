n=[1,2,3,4]
new=[i**2 for i in n]
print(new)


n=[1,2,3,4]
new=[i**2 for i in n if i%2!=0]
print(new)



fruits=['banana','apple','orange','cherry','pineapple']
new=[i for i in fruits if 'n' in i]
print(new)


fruits=['banana','apple','orange','cherry','pineapple']
new=[i for i in fruits [::-1]]
print(new)


fruits=['banana','apple','orange','cherry','pineapple']
new=[i for i in fruits if len(i)>6]
print(new)

l=[56,12.6,45,90,-6,3.4,8,-5,-12,'hello','python']
new=[i for i in l if type(i)==float]
print(new)


l=[56,12.6,45,90,-6,3.4,8,-5,-12,'hello','python']
new=[i for i in l if type(i)!=str and i>0]
print(new)


l=[56,12.6,45,90,-6,3.4,8,-5,-12,'hello','python']
new=[i for i in l if type(i)==str]
print(new)


l=[56,12.6,45,90,-6,3.4,8,-5,-12,'hello','python']
new=[i for i in range(1,101) if i%3==0]
print(new)