#print(dir(object))


# class A:
#     def __setattr__(self, name, value):
#         print(name, '=', value)
#         super().__setattr__(name, value)
#
# a = A()
# a.x = 2
#
# print(vars(a))
# print(a.x)


#---------------------------------

class A:
    def __init__(self):
        self.x = 1

    # def __setattr__(self, name, value):
    #     if name == 'x' and hasattr(self, name):
    #         raise AttributeError('x is read-only')
    #     super().__setattr__(name, value)
    #
    # def __delattr__(self, name):
    #     if name == 'x':
    #         raise AttributeError('x is read-only')
    #     super().__delattr__(name)
    #

    def __getattribute__(self, name):
        print('Get attribute ', name)
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print('Getatr', name)
        return 42


a = A()
print(a.x)
#a.x = 2
print(a.y)

#---------------------

