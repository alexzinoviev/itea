# class A:
#     def __init__(self):
#         self.x = 0          # public переменная
#         self._x = 0         # private - не использовать!
#         self.__x = 0        # hidden
#
#
# a = A()
# print(a.x)
# print(a._x)
# #print(a.__x)
#
# print(vars(a))
#
# print(a._A__x)


# class A:
#     def __init__(self):
#         self.__x = 1        # hidden
#
#     def f(self):
#         print(self.__x)
#
# class B(A):
#     def __init__(self):
#         self.__x = 2
#         super().__init__()
#     def g(self):
#         print(self.__x)
#
# b = B()
# print(b.f())

#-------------

# class A:
#     def __init__(self):
#         self.a = 1
#     a = 2
#
#     def f(self):
#         print(self.a)
#     @staticmethod # позволяет вызывать функции от имени класса
#     def g():
#         print(A.a)
#     @classmethod
#     def h(cls):
#         print(cls.a)
#
# a = A()
#
# print(a.f())
# a.g()
# a.h()
# A.g()
# A.h()
# #A.f()


#-------------------

class A:
    a = 1
    @classmethod
    def f(cls):
        print(cls.a)
    @staticmethod # явно привязан к классу
    def g():
        print(A.a)

class B(A):
    a = 22

A.f()
B.f()
A.g()
B.g()