import timeit
def f():
    return 42

print(timeit.timeit('__main__.f()', number=1000000, setup='import __main__'))