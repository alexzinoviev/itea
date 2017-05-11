import advance.advance_10
import sys
import pprint
from advance.advance_10 import add
from package.t import *


# print(sys.modules['advance.advance_10'])
#
# pprint.pprint(sys.modules)

print(add(2,3))

a = 20

print(advance.advance_10.f(5))

m = 'sys'
m1 = __import__(m)
print("Limit from imported module:" ,m1.getrecursionlimit())


pprint.pprint(sys.path)

print(a)
print(b)
print(_c)
