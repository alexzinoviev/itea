# class Table:
#     pass
#
# print(Table)
# print(type(Table))
#
# table = Table()
# table1 = Table()
# print(table)
#
# table.l = 150 # свойства обьекта
# table.w = 60
# table.h = 70
# table.color = 'red'
#
# vars(table) # все свойства которые есть у обьекта
# print (vars(table))



# print ("---------------------------------------------------2--------------------")

# class Table:
#     def f(self):  # фунции в класса - принятно называть методами
#         print (self)
#         self.x = 1
#
#
# print(Table)
# print(type(Table))
#
# table = Table()
# print (table)
# print(table.f())


# print ("---------------------------------------------------3--------------------")
# class Table():
#     def __init__(self,h,l,w): # magic methods - свойства класса определяются в методе init
#         self.l = l
#         self.w = w
#         self.h = h
#
#     def get_volume(self):
#         return self.h * self.l * self.w
#
#
# table = Table(150,60,70)
# vars(table)
# print (vars(table))
# vol = table.get_volume()
# print(vol)

# print ("---------------------------------------------------3--------------------")
#инкапсуляция
# набор методов - интерефейс класса
# class A:
#     def __init__(self):
#         self.a = 0
#         self._donttouch = 0 # считается private переменная - лучше их не
#                               #использовать вообще - использовать для работы класса при его создании
#         self.__secret = 0 # к таким переменным доступа нет
#
# a = A()
# print(a.a)
# a.a = 3
# print(a.a)
# print(a._donttouch)

#-----------------------
#наследование

# class Shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return "Shape({}, {})".format(self.x, self.y)
#
#
# s = Shape(2,3)
# print(vars(s))
# print(s)
#
#
# #--------------
#
# class Circle(Shape): # наследует сlass Shape
#     def __init__(self,x,y,r):
#         Shape.__init__(self,x,y)
#         self.r = r
#
# c = Circle(2,5,10)
#
# print(c)
# print(c.r)


########

# class Shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return "Shape({}, {})".format(self.x, self.y)
#
#
# #--------------
#
# class Circle(Shape): # наследует сlass Shape
#     def __init__(self,x,y,r):
#         super().__init__(x,y)
#         self.r = r
#
# c = Circle(2,5,10)
#
# print(c)
# print(c.r)


#--------------
# полиморфизм
class Animal:
    def __init__(self,name):
        self.name = name


class Cat(Animal):
    def say(self):
        print('Maw')
    def move(self):
        print('Run')

class Frog(Animal):
    def say(self):
        print('Qua')
    def move(self):
        print('Jump')


class Snake(Animal):
    def say(self):
        print('KHHHH')
    def move(self):
        print('Crawl')

class Dog(Animal):
    def say(self):
        print('Wow')
    def move(self):
        print('Run')

#zoo = [Animal('Tom', 'Cat'), Animal('Barsik', 'Cat'), Animal('Kermit', 'Frog'), Animal('Kaa', 'Snake')]
zoo = [Cat('Tom'), Cat('Barsik'), Frog('Kermit'), Snake('Kaa'), Dog('Sharik')]

for animal in zoo:
    animal.say()
    animal.move()