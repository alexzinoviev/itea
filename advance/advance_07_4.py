# сопрограммы
# coroutine

def coroutine(f):
    gen = f()
    next(gen)
    return gen

@coroutine
def f():
    """coroutine function"""
    i = yield
    print("f: ", i)
    i = yield i + 1
    print("f: ", i)
    i = yield i + 1
    print("f: ", i)
    i = yield i + 1


def main():
    i = f.send(0)
    print('main: ', i)
    i = f.send(i+1)
    print('main: ', i)
    i = f.send(i+1)
    print('main: ', i)


main()