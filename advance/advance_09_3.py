import abc

class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def f(self):
        pass
    @abc.abstractmethod
    def g(self):
        pass
    @abc.abstractmethod
    def h(self):
        pass


class B(A):
    def h(self):
        pass

    def g(self):
        pass

    def f(self):
        pass