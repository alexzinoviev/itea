# def fact(n):
#     #n = input("n?",n)
#     if n ==0:
#         return 1
#     return n * fact(n-1)
#
#
# print(fact(5))
# ----------
#
# def f(x):
#     return 2 * x
#
# double = f
#
# print(double(2))
# -----------
#
#
# def execute(f,x):
#     return f(x)
#
# print(execute(double,2))


# ------------------
#
# def f(n):
#     def g(x):
#         return n * x
#     return g
#
# double = f(3)
# print(double(3))
# print(f(2)(5))
# --------------

# def f(x, y=2):
#     return x * y
#
# print(f(2))
# print(f(2,5))
#
#
# ---------------

# l = []
# for i in range(10):
#     def f(x):
#         return x * i
#     l.append(f)
#
# print(l)
#
#
# print(l[5](1))


#----------

# l = []
# for i in range(10):
#     def f(x, i=i):
#         return x*i
#     l.append(f)
#
# print(l)
# print(l[5](2))


# def double(x):
#     return 2 * x
#
# t = list(map(double, [1,2,3,4,5]))
# print(t)
#
# #-----------
#
# def odd(x):
#     return  x % 2
#
# k = list(filter(odd, [1,2,3,4,5,6,7]))
# print(k)
#
# #----------
#
#
# def map_(f,l):
#     l_new = []
#     for i in l:
#         l_new.append(f(i))
#     return l_new
#
# n = map_(double, [1,2,3,4,5])
# print(n)
#
#
#
# #---------------
# import functools
# def add(x,y):
#     return x + y
# f = functools.reduce(add, [1,2,3,4,5])
# print(f)
#
# def mul(x,y):
#     return x*y
# functools.reduce(mul, [1,2,3,4,5])
#
# #-----------
#
# m = list(map(lambda x: 2*x, [1,2,3,4,5]))
# print(m)
#
#
# a = functools.reduce(lambda a,x: x, [1,2,3,4,5])
# print(a)
#
# a1 = functools.reduce(lambda a,x: a + x, [1,2,3,4,5])
# print(a1)
#
#
# list1 = [2*x for x in [1,2,3,4,5]]
# print(list1)
#
# list2 = [2*x for x in [1,2,3,4,5] if x % 2]
# print(list2)
#
#
#
# min_1 = min(1,2,3,4,5)
# print(min_1)
#
# #------
#
# def f(*args):
#     print(args)
#
# f(1,2)
#
#
# def sum_(*args):
#     s = 0
#     for i in args:
#         s+= i
#     return s
#
# sum1 = sum_(1,2,3,4,5,)
# print(sum1)
#
#
# def f(*args, **kwargs): #  позиционные и именованые
#     print(args, kwargs)
#
# f(1,2,3,a=4,b=5,c=8)
#
#-------------

# def f(price, kg = None, g = None):
#     if g is not None:
#         kg = g / 1000
#     return  kg*price
#
# f1 = f(5,2)
# print(f1)

#-----

# def f2(price, * ,kg = None, g = None):
#     if g and kg:
#         raise ValueError
#     if g is not None:
#         kg = g / 1000
#     return  kg*price
#
# f3 = f2(5, g=2)
# print(f3)

# def f(a,b,c):
#     return a+b+c
#
# t = 1,2,3
# print(f(*t)) # распаковка
#
# d = {'a':1, 'b':2, 'c':3}
# print(f(**d))
# print(f(*d))
#
#
#
# #---------------
#
# l = list(zip([1,2,3], [4,5,6]))
# print(l)

#------------
#
# m = [[1,2,3],[4,5,6],[7,8,9]]
# m_l = list(zip(*m))
# print(m_l)
#

#-----------

#декораторы

# def get_area(x):
#     return x*x
#
# def scale(f):
#     def wrapper(x):
#         print('In wrapper')
#         res = f(x*100)
#         print('out wrapper')
#         return res
#     return wrapper
#
# get_area = scale(get_area)
#
# print(get_area(5))

#----------

#need to debug it
# def scale(f):
#     def wrapper(x):
#         print('In wrapper')
#         res = f(x*100)
#         print('out wrapper')
#         return res
#     return wrapper
#
# @scale
# @scale
# def get_area(x):
#     return x*x
#
# print(get_area(5))

#----------

def log(f):
    print('In log')
    def wrapper(*args, **kwargs):
        print("Params", args, kwargs)
        res = f(*args, **kwargs)
        print("Result", res)
    print('Out log')
    return wrapper

@log
def add(x,y):
    return x+y

add(2,3)