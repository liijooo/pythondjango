s="hello"
for i in s:
    print(i)
    if(i=='l'):
        break

fruits=['banana','apple','orange','pineapple','mango']
for i in fruits:
    if(i=='pineapple'):
        break
    print(i)
print()

fruits=['banana','apple','orange','pineapple','mango']
for i in fruits:
    if(i=='apple'):
        continue
    print(i)
print()

l=[45,67,12,90,78,10]
for i in l:
    if(i%3==0):
        continue
    print(i)


s="python is a programming language"
for i in s:
    print(i,end="")
    if(i=='s'):
        break