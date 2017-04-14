import numbers

class Number:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return "Number({})".format(self._n)
    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Number(self._n + other)
        return Number(self._n + other._n)

    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)




n = Number(5)

print(n)

print(Number(5) + Number(4) + Number(3))

print(Number(5) + 5)
