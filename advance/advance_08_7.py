# class A:
#     def __new__(cls):
#         return 42
#
# a = A()
#
# print(a)
# print(type(a))


print('------------------------------------')


class Car:
    def run(self):
        print('Rrrrr')


class Truck:
    def run(self):
        print('Zhhh')


class Vehicle:
    def __new__(cls, type_):
        if type_ == 'Car':
            return Car()
        elif type_ == 'Truck':
            return Truck()
        else:
            raise ValueError


vehicles = ['Car', 'Truck', 'Car', 'Car']
vehicles = [Vehicle(x) for x in vehicles]
print(vehicles)


for vehicle in vehicles:
    vehicle.run()


print('-------------------------------')

class Singletone:
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

s = Singletone()
s1 = Singletone()
print(s is s1)