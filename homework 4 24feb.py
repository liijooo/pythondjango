n=[23,-9,11,24,37,-16,90,-3,-4,-51]
import functools
sum_even=list(filter(lambda x:x>0 and x%2==0,n))
print(functools.reduce(lambda x,y:x+y,sum_even))
sum_odd=sum(filter(lambda x:x>0 and x%2!=0,n))
print(sum_odd)
sum_negative_even=sum(filter(lambda x:x<0 and x%2==0,n))
print(sum_negative_even)
sum_negative_odd=sum(filter(lambda x:x<0 and x%2!=0,n))
print(sum_negative_odd)
count_even=len(list(filter(lambda x:x>0,n)))
print(count_even)
count_odd=len(list(filter(lambda x:x<0,n)))
print(count_odd)


l=[10,'hello',9.8,'abc',11.2,'arun']
print(list(filter(lambda x:type(x)==str,l)))
print(list(filter(lambda x:type(x)==float,l)))