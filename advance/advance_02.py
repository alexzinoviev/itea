# def f(a=None):
#     if a is None:
#         return 42
#     return a
#
#
# print(f(None))
# print(f([1,2,3]))
#
#
# #---------------------------------
# print ('-------------------------------1')
# #---------------------------------
#
#
# sentinel = object()
# def f1(a=sentinel):
#     if a is sentinel:
#         return 42
#     return a
#
#
# print(f1(2))
# print(f1(None))
# print(f1(object()))
#
# #---------------------------------
# print ('-------------------------------2')
# #---------------------------------
#
# print(min(1,2,3))
#
# def f2(*args):
#     print(args)
#
# f2(1,2,3,4)
#
# #---------------------------------
# print ('-------------------------------3')
# #---------------------------------
#
# def sum_(*args):
#     s = 0
#     for arg in args:
#         s+=arg
#     return s
#
# print(sum_(1,77,22,49))
# print(sum_())
#
# #---------------------------------
# print ('-------------------------------4-specify first required parameter')
# #---------------------------------
#
# def sum_(a, *args):
#     for arg in args:
#         a+=arg
#     return a
#
# print(sum_(1,77,22,49))
# print(sum_(1))
#
# #---------------------------------
# print ('-------------------------------5')
# #---------------------------------
#
# def f4(*args, **kwargs):
#     print(args, kwargs)
#
# f4(1,2,3,a=3,b=4)
#
# #---------------------------------
# print ('-------------------------------6')
# #---------------------------------
#
# def price(cost, kg=None, g=None):
#     if kg is not None:
#         return cost*kg
#     elif g is not None:
#         return cost*0.001*g
#     else:
#         raise ValueError
#
# print(price(2,5))
# print(price(2,kg=5))
# print(price(2,g=500))
#
# #---------------------------------
# print ('-------------------------------7')
# #---------------------------------
#
# def price2(cost,*, kg=None, g=None):
#     if kg is not None:
#         return cost*kg
#     elif g is not None:
#         return cost*0.001*g
#     else:
#         raise ValueError
#
# #print(price2(2,5)) # error not positional parameter
# print(price2(2,kg=5))
# print(price2(2,g=500))
#
#
# #---------------------------------
# print ('-------------------------------8')
# #---------------------------------
#
# def f5(a,b,c):
#     return a+b+c
#
# t = 1,4,7
#
# print(f5(1,3,4))
# print(f5(*t))
#
# #---------------------------------
# print ('-------------------------------9')
# #---------------------------------\
#
# def g(a,b,c):
#     return a + b + c
#
# def g1(*args, **kwargs):
#     print('*******')
#     return g(*args, **kwargs)
#
# print(g1(1,2,5))
#
# #---------------------------------
# print ('-------------------------------10')
# #---------------------------------\
#
# d = {'a':1, 'b':2, 'c':3}
# price(g1(d))

#---------------------------------
# print ('-------------------------------11')
# #---------------------------------\
#
# def f():
#     a = 1
#     print(locals())
#
# f()

#---------------------------------
print ('-------------------------------12')
#---------------------------------\
#
# def f():
#     a = 2
#     def g():
#         a = 3
#         print(a)
#     print(a)
#     g()
#
# f()


#---------------------------------
print ('-------------------------------13')
#---------------------------------\

# def f(x):
#     return 2*x
#
# double = f
#
# print(double(2))


#---------------------------------
print ('-------------------------------14')
#---------------------------------\
#
# import functools
# def add(x,y):
#     return x+y
#
# t = functools.reduce(add, [1,2,3,4,5])
# print(t)
#
#
# #---------------------------------
# print ('-------------------------------15')
# #---------------------------------\
#
# print([2*x for x in [1,2,3,4,5]])
# print([(x,y) for x in [1,2,3] for y in [4,5,6]])
#
#
# #---------------------------------
# print ('-------------------------------16')
# #---------------------------------\
#
# print(list(map(lambda x:2*x, range(10))))


#---------------------------------
print ('-------------------------------17')
#---------------------------------\

# import operator
#
# print(operator.add(2,3))

#---------------------------------
print ('-------------------------------18')
#---------------------------------\
# import functools
# import operator
#
# double = functools.partial(operator.mul, 2)
# print(double(3))
#
# inc = functools.partial(operator.add, 1) # частично параметер фиксируется, а второй будет передаваться при вызове функции
# print(inc(2))


#---------------------------------
print ('-------------------------------19')
#---------------------------------\
#
# def composition(f,g):
#     return lambda x: f(g(x))

#---------------------------------
print ('-------------------------------20')
#---------------------------------\
# import operator
#
# l = [(2,1), (3,2), (2,3), (4,2), (2,4), (1,5)]
# l.sort()
# print(l)
#
# l.sort(key=lambda x: x[1])
# print(l)
#
# l.sort(key=operator.itemgetter(1))
# print(l)
#
# l1 = [(1,1), (3,4), (2,2)]
# l1.sort(key=lambda x:x[1])
# print(l1)
#
# l2 = [1, 'a', 3.4]
# l2.sort(key=str)
# print(l2)
#---------------------------------
print ('-------------------------------21')
#---------------------------------\

# def f(a):
#     def g(x):
#         return a * x
#     return g
#
# double = f(2)
# triple = f(3)
#
# print(double(4))
# print(triple(3))

#---------------------------------
print ('-------------------------------22') # need to debug it
# #---------------------------------\
# f
# f.a = 1

# def f(a):
#     def g(x):
#         return a * x
#     def set_a(x):
#         nonlocal a
#         a = x
#     g.set_a = set_a
#     return g
#
# double = f(2)
# print(double(3))
#
# double.set_a(5)
# print(double(3))

#---------------------------------
print ('-------------------------------23') # need to debug it
# #---------------------------------\

# l = []
# for i in range(10):
#     def f(x, a=i):
#         return a*x
#     l.append(f)
#
#
# print(l)
# print(l[1](2))

#---------------------------------
print ('-------------------------------24') # need to debug it
# #---------------------------------\

# def get_area(x):
#     return x*x
#
# def scale(f):
#     def wrapper(x):
#         return f(x*10)
#     return wrapper
#
# get_area = scale(get_area)
#
# print(get_area(5))

#---------------------------------
print ('-------------------------------25') # need to debug it
# #---------------------------------\


# def scale(n):
#     def decorator(f):
#         def wrapper(x):
#             return f(x*n)
#         return wrapper
#     return decorator


#@scale(5)
# def get_area(x):
#     return x*x
#
# print(get_area(10))

#---------------------------------
print ('-------------------------------25') # need to debug it
# #---------------------------------\


# @scale(5)
# def get_area(x):
#     '''Calculate area'''
#     return x*x
#
# print(get_area)



#---------------------------------
print ('-------------------------------25') # need to debug it
# #---------------------------------\
import functools

def scale(f):
    @functools.wraps(f)
    def wrapper(x):
        return f(x*10)
    return wrapper


@scale
def get_area(x):
    '''Calculate area'''
    return x*x

print(get_area)