n=int(input("enter number"))
for i in range(1,11):
   print(n,'*',i,'=',n*i)


l=[1,1,2,3,4,4,5,6,7]
new=[]
for i in l:
   if i not in new:
       new.append(i)
       print(new)
print()


#s="hello world"
#new=" "
#for i in s:
 #   if i not in new and i!=" ":
  #      new=new+i
#print(new)
#print()

d={'country1':'india','country2':'myanmar','country3':'newzealand','country4':'iceland','country5':'england'}
for i in d.values():
    if('land' in i):
        print(i)