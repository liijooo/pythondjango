def func(name,age):
    print("name is",name,"age is",age)

func("arun",23)


def func(*args):
    print(args[0])

func('arun')
func('amal','vis')
func('ko','vo','ro')
func(1,2,3,4,5,6,7,8,9)


def func(**kwargs):
    print(kwargs)


func(arun=20,amal=19)


def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum(1,2,3,4,5,6,7)
sum(20,30,40,50)
