"""слабые ссылки"""

import weakref, sys


class A:
    pass

a = A()

print(sys.getrefcount(a))

b = weakref.ref(a)
print(b)

print(sys.getrefcount(a))
print(b())