"""
yield

1. итераторы
2. ленивые вычисления
3. сопрограммы


"""
# ленивые вычисления

def infinity_list():
    i = 0
    while True:
        yield i
        i+=1

g = infinity_list()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for i in infinity_list():
    if i*i > 100:
        break
    print(i, i*i)


#----------------------

import itertools
t = list(itertools.takewhile(lambda x: x < 100, (x*x for x in itertools.count(0))))

print(t)

print('-------------------------------------------------------------------------------------')

l =[0] * 5 + [1] * 2 + [0] * 3 + [1] * 5
print(l)

for i,j in itertools.groupby(l):
    print(i, list(j))


for i,j in itertools.groupby(l):
    print(i, len(list(j)))

print('-------------------------------------------------------------------------------------')

