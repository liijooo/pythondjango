# x=123
# for i in x:
#     print(x)

s='abcd'
print(s[2:])


# d={0:'a',1:'b',2:'c'}
# for x in d.values():
#     print(d[x])


d = {0: 'a', 1: 'b', 2: 'c'}
for i in d:
    print(i)


x={'ab','cd'}
for i in x:
    i.upper()
print(x)

i = 1
while True:
    if i % 3 == 0:
        break
    print(i)

    i += 1


# i = 1
# while True:
#     if i%2 == 0:
#         break
#     print(i)
#     i += 2


# for i in range(10):
#      if i == 5:
#          break
#      else:
#          print(i)
# else:
#     print("Here")



z=set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)



list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)



# x = 'abcd'
# for i in range(len(x)):
#     print(i)



# a = [1, 2, 3]
# a = tuple(a)
# a[0] = 2
# print(a)


for i in range(3):
      if(i>0):
           print(i*100)


# def thrive(n):
#  if n % 15 == 0:
#    print("thrive", end = "")
#  elif n % 3 != 0 and n % 5 != 0:
#    print("neither", end = "")
#  elif n % 3 == 0:
#    print("three", end ="")
#  elif n % 5 == 0:
#    print("five", end = "")
# thrive(35)
# thrive(56)
# thrive(15)
# thrive(39)
#
#
#
# a = [1, 2]
# print(a * 3)
#
#
#
# dict1 = {'first' : 'sunday', 'second' : 'monday'}
# dict2 = {1: 3, 2: 4}
# dict1.update(dict2)
# print(dict1)
#
#
#
# word = "Python Programming"
# n = len(word)
# word1 = word.upper()
# word2 = word.lower()
# converted_word = ""
# for i in range(n):
#  if i % 2 == 0:
#    converted_word += word2[i]
#  else:
#    converted_word += word1[i]
# print(converted_word)



# a = "4, 5"
# nums = a.split(',')
# x, y = nums
# int_prod = int(x) * int(y)
# print(int_prod)



# square = lambda x: x ** 2
# a = []
# for i in range(5):
#    a.append(square(i))
#
#
# def tester(*argv):
#    for arg in argv:
#        print(arg, end = ' ')
# tester('Sunday', 'Monday', 'Tuesday', 'Wednesday')
#
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {2, 4, 6}
# print(s1 ^ s2)
#
#
#
# for i in range(100,201):
#     sum=0
#     for even in str(i):
#         sum+=int(even)
#     if sum%2==0:
#         print(i)
#
#
# for i in range(1,101):
#     if(i%3==0):
#         print("fizz")
#     elif(i%5==0):
#         print("buzz")
#     elif(i%3==0 and i%5==0):
#         print("fizzbuzz")
#
#
# l=[1,2,3]
# sum1=l[1]+l[2]
# sum2=l[0]+l[2]
# sum3=l[0]+l[1]
# sum=(sum1,sum2,sum3)
# print(sum)


# def prime():
#     l = [23,12,11,56,74,80,36,39]
#     for i in l:
#         if(i>1):
#             for j in range(2,i):
#                 if(i%j==0):
#                     break
#             else:
#                 print(i,"prime number")
# prime()



s="malayalam is a language"
count=s.split()
print(len(count))
maximum=max(s.split(),key=len)
print(maximum)
for i in s.split():
    if i==i[::-1]:
        print("palindrome",i)



# def bmi_value(weight,height):
#     bmi=weight/(height/100)**2
#     return bmi
# height=float(input("enter the weight"))
# weight=float(input("enter the height"))
# final_value=bmi_value(weight,height)
# print(final_value)



for i in range(1,5):
    for j in range(i,0,-1):
        print(j,end=" ")

    print()



