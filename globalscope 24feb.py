#x=10
#print(x)     #global variable

#def f():
#    print('inside',x)
#print('outside',x)
#f()
#print('outside',x)




#def f():
#    global x
#    x=20    #local variable
#    print(x)

#f()
#print(x)



# def outer():
#     x=20
#     print(x)
#     def inner():
#         print(x)
#
#     inner()
# outer()


def outer():
    x=20
    print('inside outer',x)
    def inner():
        nonlocal x
        x=x+1
        print('inside inner',x)
    inner()
    print('outside inner',x)
outer()