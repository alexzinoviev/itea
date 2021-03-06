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
        return MyListIterator(self._l)

class MyListIterator:

    def __init__(self, l):
        print('Iter')
        self._l = l
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('Next')
        self._i+=1
        if self._i == len(self._l) + 1:
            raise StopIteration
        return self._l[self._i - 1]



# l = MyList([1,2,3])
# print("l", l)
#
# l1 = [1,2,3]
#
# l = MyList(l1)
#
# print("l", l)
# print("l1", l1)
#
# l1[0] = 0
#
# print("l", l)
# print("l1", l1)
#
# print(len(l))
#
# l2 = MyList([])
# print(bool(l2))
#
#
# print(1 in l)
#
# print(l[0])
# l[0] = 0
# print(l[0])
#
#
# # print(dir(l1))
# # print(dir(l))
#
#
# def f():
#     print("1")
#     ...
#     print("2")
#
# print("Elippsis", f())
#

#-------------
# l = MyList(range(10))
# print("l", l)
#
# print(l[3])
#
# print(l[1,3,5,7])
# print(l[...])

l = MyList([1,2,3])
print(l)
# for i in l:
#     print(i)

for i in l:
    for j in l:
        print(i, j)