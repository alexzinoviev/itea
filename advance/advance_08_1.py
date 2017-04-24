# def f():
#     for i in range(5):
#         yield i
#
# g = f()
# print(next(g))
# print(next(g))
# print(g.send(1))
# g.close()
# next(g)


def f():
    fn = open('test.txt', 'rt')
    for line in fn:
        try:
            yield line
        except GeneratorExit:
            fn.close() # если нам надо чтото искать в файле - мы можем вызвать метод close когда мы нашли то что нам надо
            break


g = f()
print(next(g))
print(next(g))
g.close()
print(next(g))