from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    print(a*b)

@dispatch(int,int,int)
def product(a,b,c):
    print(a*b*c)

@dispatch(float,float,float)
def product(a,b,c):
    print(a*b*c)

product(10,20)
product(10,20,30)
product(1.2,3.23,3.33)