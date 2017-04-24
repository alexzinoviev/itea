import profile


class memo:
    def __init__(self):
        self._state = {}

    def __call__(self, f):
        def wrapper(n):
            if n not in self._state:
                self._state[n] = f(n)
            return self._state[n]
        return wrapper

@memo()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))
profile.run('fib(100)')