# class AbstractObject:
#     def __init__(self, *args, **kwargs):
#         pass
#
# class Shape(AbstractObject):
#     def __init__(self, *args, **kwargs):
#         self.x, self.y = kwargs['x'], kwargs['y']
#         super().__init__(*args, **kwargs)
#
# class ColoredObject(AbstractObject):
#     def __init__(self, *args, **kwargs):
#         self.color = kwargs['color']
#         super().__init__(*args, **kwargs)
#
#
# class ColoredCircle(Shape, ColoredObject):
#     def __init__(self, *args, **kwargs):
#         self.r = kwargs['r']
#         super().__init__(*args, **kwargs)
#
#
# class ColoredTriangle(ColoredObject, Shape):
#     def __init__(self, *args, **kwargs):
#         self.a = kwargs['a']
#         super().__init__(*args, **kwargs)
#
#
# c = ColoredCircle(x=1,y=2,color=3, r=3 )
# vars(c)
# print(vars(c))



class Shape():
    def __init__(self, *args, **kwargs):
        self.x, self.y = kwargs['x'], kwargs['y']
        super().__init__(*args, **kwargs)

class ColoredObject():
    def __init__(self, *args, **kwargs):
        self.color = kwargs['color']
        super().__init__(*args, **kwargs)


class ColoredCircle(Shape, ColoredObject):
    def __init__(self, *args, **kwargs):
        self.r = kwargs['r']
        super().__init__(*args, **kwargs)


class ColoredTriangle(ColoredObject, Shape):
    def __init__(self, *args, **kwargs):
        self.a = kwargs['a']
        super().__init__(*args, **kwargs)
