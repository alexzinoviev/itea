class Line:
    def __init__(self):
        self._l = 0
    @property
    def l(self):
        return self._l / 9
    @l.setter #будет выполняться вместо setter код ниже
    def l(self, value):
        self._l = 9 * value


class Box:
    def __init__(self, l, w, h):
        self._l, self._w, self._h = l, w, h
    @property
    def volume(self):
        return self._l * self._w * self._h

b = Box(10, 20, 30)
print(b.volume)