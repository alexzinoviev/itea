class ReprMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ','.join([
                "{}={}".format(name, value)
                for name, value in self.__dict__.items()
                ]
            )
        )

class EqualMixin:
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__



class Person(ReprMixin, EqualMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Bill', 12)
print(p)

print(Person('Bill', 12) == Person('Bill', 12))