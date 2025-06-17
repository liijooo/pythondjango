l1=[12,34,45,67,90]
l2=[56,23,34,78,12,55]
set1=set(l1)
set2=set(l2)
intersection_set=set1.intersection(set2)
print(intersection_set)


d={1:['arun',20000],2:['amal',30000],3:['anu',15000]}
salary=[]
for value in d.values():
    salary.append(value[1])

max_salary=max(salary)
print(max_salary)

l=[12,34,56,67,22]
maximum=0
for i in l:
    if(i>maximum):
        maximum=i
print(maximum)


s="python is a programming language"
string=s.split()
maximum=max(string,key=len)
print(maximum)

l=[1,1,1,2,3,3,5,5,5,6]
occurences={}
for i in l:
    if i not in occurences:
        occurences[i]=l.count(i)
print(occurences)
