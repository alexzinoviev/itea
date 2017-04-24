def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

class Notifier:
    def __init__(self):
        self.observers = []
    def register(self, observer):
        self.observers.append(observer)
    def unregister(self, observer):
        self.observers.remove(observer)
    def __call__(self, f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            for observer in self.observers:
                observer()
            return res
        return wrapper



# def notify(f):
#     def wrapper(*args, **kwargs):
#         res = f(*args, **kwargs)
#         for observer in observers:
#             observer()
#         return res
#     return wrapper

notifier = Notifier()


@notifier
def f():
    return 42


print(f())
#
# observers.append(b())
# observers.append(a())

f()

# Notifier().register(a())
# Notifier().register(b())
# Notifier().unregister(a())

notifier.register(a())
notifier.register(b())
notifier.unregister(a())