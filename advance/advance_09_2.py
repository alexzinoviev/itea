# A = type('A', (object, ), {'a': 1})
#
# print(A.a)


"""метклассы"""
#
# class Meta(type):
#     """мета класс - наследуется от класса type"""
#     def __new__(cls, name, parents, props):
#         new_props = {}
#         for name, value in props.items():
#             if not name.startswith('unused_'):
#                 new_props[name] = value
#         return super().__new__(cls, name, parents, new_props)
#
#
# class A(metaclass=Meta):
#     a = 1
#     unused_a = 1
#
# print(dir(A))


print("--------------------------------")

# class Meta(type):
#     def __call__(*args, **kwargs):
#         instance = type.__call__(*args, **kwargs)
#         instance.a = 1
#         return instance
#
#
# class A(metaclass=Meta):
#     pass
#
# a = A()
#
# print(a.a)


print("--------------------------------")

# class Meta(type):
#     def __call__(*args, **kwargs):
#         print('Call')
#         return type.__call__(*args, **kwargs)
#
#     def __new__(*args, **kwargs):
#         print('New')
#         return type.__new__(*args, **kwargs)
#
#     def __init__(*args, **kwargs):
#         print('Init')
#         type.__init__(*args, **kwargs)
#
#
# class A(metaclass=Meta):
#     pass
#
# print("-----")
#
# a = A()


print("--------------------------------")


class Meta(type):
    def __new__(cls, name, parents, props):
        new_cls = super().__new__(cls, name, parents, props)
        if hasattr(cls, 'children'):
            cls.children[name] = new_cls
        else:
            cls.children = {}
        return new_cls


class A(metaclass=Meta):
    pass

class B(A):
    pass

print(A.children)


class C(B):
    pass

print(A.children)