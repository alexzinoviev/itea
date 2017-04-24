# class A:
#     def __init__(self):
#          self.a = 1
#
#     def __enter__(self):
#         print('Enter')
#
#     def __exit__(self, *args, **kwargs):
#         print('Exit')
#
#
# with A() as a:
#     pass
#
#
# with A():
#     pass


#-------------------

# позволяет вызывать метод класса как функцию

# class Multiplier:
#     def __init__(self, n):
#         self._n = n
#
#     def __call__(self, x):
#         print('Call')
#         return self._n * x
#
# double = Multiplier(2)
# print(double(2))

#-------------------

# class scale:
#     def __init__(self, n):
#         self._n = n
#     def __call__(self, f):
#         def wrapper(x):
#             return f(x * self._n)
#         return wrapper
#
# @scale(5)
# def get_area(x):
#     return x * x
#
# print(get_area(5))


#-------------------

import profile


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


#print(fib(20))

profile.run('fib(40)')