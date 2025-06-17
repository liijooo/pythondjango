#Question1
#declare 5 food items
l=['burger','pizza','biriyani','icecream','cake']
#add a new food item
l.append('porotta')
print(l)
#print the last food item
print(l[-1])
#replace the food item value at the 3rd index
l[3]='idli'
print(l)
#print the length
print(len(l))
#reverse
print(l[::-1])

#Question2
l=[23,45,67]#find the average
a=l[0]
b=l[1]
c=l[2]
sum=a+b+c
average=sum/3
print("average is:",average)

#Question3
s="python is a highlevel programming language"
#length
print(len(s))
#reverse
print(s[::-1])
#13th character
print(s[12])
#print the characters from 2nd index to 10th index
print(s[2:10])

#Question4
d={1:{'title':'ABC','author':'john','price':200},2:{'title':'PQR','author':'mike','price':300},3:{'title':'STU','author':'sam','price':250}}
#print all the title values
print(d[1]['title'],d[2]['title'],d[3]['title'])

#print length
print(len(d))
#print the average price
a=(d[1]['price'])
b=(d[2]['price'])
c=(d[3]['price'])
sum=a+b+c
average=sum/3
print("the average is:",average)
