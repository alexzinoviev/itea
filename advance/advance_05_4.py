class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person({}, {})'.format(self.name, self.age)

    def __eq__(self, other): # переопределяет метод сравнения
        if not isinstance(other, Person):
            return NotImplemented
        else:
            return self.name == other.name #and self.age == other.age

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other): # less then - метод сравнения
        return self.name < other.name



l = [Person('Bob', 23), Person('Bill', 32), Person('John', 32), Person('Bob', 77)]
l.sort()

print(l)

#-------------------

# s = {Person('Bob', 23), Person('Bill', 32), Person('John', 32), Person('Bob', 77)}
# print(s)
#
# p = Person('Bill', 32)
# d = {p:1}
# print(d)
# print(d[p])
#
# p.name = 'Mary'
# print(d)
# print(d[p])

#-------------------

# p = Person('Bill', 32)
# p1 = Person('Bill', 32)
# p2 = 'ttt'
#
# print(p == p1)
# print(p == p2)
#
# l = [Person('Bob', 23), Person('Bill', 32), Person('John', 32)]
# l1 = l.index(Person('Bill', 32))
# print(l1)




# обработка Null objects
# class NullObject:
#     def __getattr__(self, name):
#         logger.info('some')
#         return object()