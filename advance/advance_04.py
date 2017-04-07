# class new():
#     print("class")
#
# a = new()
#
# print(a)
# print(a.__dict__)
# a.__dict__['x'] = 1
# print(a.__dict__)
#
# print(a.x)
# a.x = 2
# print(a.x)
# del a.x
# print(a.__dict__)
# a.x = 3
#
# vars(a)
# print(vars(a))

#------------------------------

# class A:
#     a = 1 # переменная класса - статическая - которя будет доступна во всех экземплярах класса
#
# a = A()
#
# print(a.a) # доступ к элементу через переменную(экземпляр) класса (в локальной области видимости)
# print(A.a) # доступ к элементу через клас
#
# a.a = 2
# print(a.a) #
# print(A.a) # доступ к элементу через клас
#
# A.b = 3
# print("variable", a.b) #
# print("class", A.b) # доступ к элементу через клас


#---------------------------
# классы нам нужны для методов
#
# class A:
#     def f(self): # принято первым параметром метода называть self
#         print(self)
#         self.x = 1
#
#
# a = A()
# a.f()
# #print(a.f())
# print(a)
# print(a.x)
# # от класса вызвать метод нельзя - можно вызвать только от экземпляра A.f()
#
# class B:
#     pass
# b = B()
# A.f(b)
#
# print(b.x)
#
#
#---------------------------

# class A:
#     def f(self):
#         print('A')
#
# class B:
#     def f(self):
#         print('B')
# #
#
# a = A()
# a.f()
# a.__class__ = B # экземпляр класса А присвоили классу B
# a.f()

#---------------------------

# class A:
#     def __init__(self, a, b): # magic method - будет автоматически вызываться при создании каждого экземпляра класса
#         self.a = a
#         self.b = b
#
#
# a = A(1,2)
# vars(a)
# print(vars(a))
#
# #---------------------------
# print(B.__base__)
#
#
#---------------------------

# class A:
#     def f(self):
#         print('A')
#
# class B(A): # наследует класс А
#     pass
#
#
# a = B()
# a.f()
#
# a.g()

#---------------------------

class Shape:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y) # переопределение метода в классе наследнике - использовать super чтобы не повторять так можно вызывать любой метод класса родителя
        self.r = r

c = Circle(1,2,3)
vars(c)
print(vars(c))

print(c)
print(repr(c))

print(dir(object))

"""переопределение magic метода __repr__"""
Circle.__repr__ = lambda self: 'Circle({},{},{})'.format(self.x, self.y, self.r)

print(c)


print(str(c))

Circle.__str__ = lambda self: 'Circle: x={}, y={}, r={}'.format(self.x, self.y, self.r)

print(repr(c))
print(str(c))


#---------------------------

class ReprMixin:
    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ','.join(
                ['{} = {}'.format(name, value) for  name, value in self.__dict__.items()]
            )
        )


class A(ReprMixin):
    def __init__(self,a, b):
        self.a, self.b = a, b

a = A(1,2)
print(a)


class CircleWithRepr(Circle, ReprMixin):
    pass


c = CircleWithRepr(1,2,3)
print(c)


# движемся слева направо по списку наследования
# движемся снизу вверх