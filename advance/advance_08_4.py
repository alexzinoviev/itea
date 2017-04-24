import pickle

class A:
    def __init__(self, f):
        self.f = f
        self.a = 1

    def __getstate__(self):
        print('Get state')
        d = self.__dict__.copy()
        del d['f']
        return d

    def __setstate__(self, obj):
        print('Set state')
        self.__dict__ = obj
        self.f = lambda x: 2*x


a = A(lambda x: 2* x)
print(vars(a))

s = pickle.dumps(a)
print(s)

b = pickle.loads(s)
print(b)

with open('file.txt', 'wt') as f:
    f.write('String\n')