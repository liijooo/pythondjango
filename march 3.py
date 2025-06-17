# for i in range(100,201):
#     sum=0
#     for j in str(i):
#         sum+=int(j)
#     if sum%2==0:
#         print(i)

l=[3,7,1,2,8,4,5]
for i in range(1,9):
    if i not in l:
        print(i)


vehicles=['car','bike','bus','train','flight']
for i in vehicles:
    if(i[0]!='b'):
        print(i)