# import sys
#
# a = 1
# b = 2
# c = 1
# print(id(a))
# print(id(1))
# print(id(b))
#
# print(a is b)
#
# print(sys.getrefcount(1))
#
# print ('--------------------')
#
# l = [1,2,3]
# l.append(l)
#
# print(l)

#---------------------------------
# print ('-------------------------------')
#---------------------------------

import gc # garbage collector
d = {}
for i in range(10):
    d = {}
    d['a'] = d

print(d)
print(gc.collect())

#---------------------------------
print ('-------------------------------')
#---------------------------------

print(1_000_000)

#---------------------------------
print ('-------------------------------')
#---------------------------------

import math
print(math.isclose(0.1+0.2, 0.3))


a = .1+.1+.1+.1+.1+.1+.1+.1+.1+.1
print(a)

b = math.fsum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])
print(b)

#---------------------------------
print ('-------------------------------')
#---------------------------------
import decimal
c = decimal.Decimal('0.1') + decimal.Decimal('0.2')
print(c)

#---------------------------------
print ('-------------------------------')
#---------------------------------

a1 = 'Привет!'
b1 = a1.encode('utf8')
print(b1)
c1 = b1.decode('utf8')
print(c1)

#---------------------------------
print ('-------------------------------')
#---------------------------------

name = 'Bob'
age = 22

s = f'Name: {name}, age: {age}'
print(s)

#---------------------------------
print ('-------------------------------')
#---------------------------------


