class MyList:
    def __init__(self, l):
        #self._l = l.copy()
        self._l = list(l) # защита от изменения внешнего состояния, и всегда будет списком

    def __repr__(self):
        return repr(self._l)

    def add(self,a ):
        self._l.append(a)

    def __len__(self):
         return len(self._l)

    def __bool__(self):
        return bool(self._l)

    def __contains__(self, obj):
        return obj in self._l

    def __setitem__(self, index, value):
        self._l[index] = value

    def __getitem__(self, index):
        #return self._l[index]
        #print(index)
        if isinstance(index, int):
            return self._l[index]
        elif isinstance(index, tuple):
            return [self._l[i] for i in index]
        elif index == ...:
            return self._l.copy()
        else:
            raise IndexError

    def __iter__(self):
        for i in self._l:
            yield i

l = MyList([1,2,3])
print(l)

for i in l:
    for j in l:
        print(i, j)