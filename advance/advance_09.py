"""
дескрипторы
когда обращаемся к экземпляру класса
дескриптор - класс который реализует методы set и get
"""

# class Length:
#     """
#     будет реализовывать метод дескриптора
#     """
#     def __set__(self, obj, value):
#         obj._l = 10 * value
#
#     def __get__(self, obj, objtype):
#         return obj._l / 9
#
#
# class Line:
#     l = Length()
#
#     def __init__(self):
#         self._l = 0
#
#
# a = Line()
# a.l = 10
# print(a.l)
# print(a._l)

# print('---------------------------')
#
# class Volume:
#     def __get__(self, obj, objtype):
#         return obj._l * obj._w * obj._h
#
# class Box:
#     def __init__(self, h, w, l):
#         self._h, self._w, self._l = h, w, l
#     volume = Volume()
#
# b = Box(10, 20, 30)
# print(b.volume)
# b._l = 40
# print(b.volume)


import collections
d1 = {'a': 2, 'b': 3}
d1 = {'a': 5, 'b': 3}
d2 = {'a': 2, 'b': 3}

d = collections.ChainMap(d1, d2)

print(d[a])