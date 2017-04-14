class A:
    def m1(self):
        print('A.m1')
    def m2(self):
        print('A.m2')


class Proxy:
    def __init__(self):
        self.a = A()
    def m1(self):
        print('Proxy.m1')
    def __getattr__(self, name):
        return getattr(self.a, name)


p = Proxy()
print(p.m1())
print(p.m2())