#count and sum divisible by 5
sum=0
count=0
l=[10,43,23,90,18,16,78,34]
for i in l:
    if(i%5==0):
        count+=1
        sum=sum+i
print("count is",count)
print("sum is",sum)
print()


#count of vowels
count=0
s="hello world"
vowels='aeiou'
for i in s:
    if i in vowels:
        count+=1
        print(i)
print("count is",count)
