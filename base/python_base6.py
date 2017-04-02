# # ASCII symbols
# for i in range(32,127):
#     print(chr(i), end='')
#


# import string
# import random
#
# string_var = string.digits
# print(string_var)
#

#-------------------------
# name = 'Bill'
# age = 23
# result = "Name: " + name + "; age: " + str(age)
# print(result)
#
# result2 = "Name: %s; age: %d" % (name, age)
# print(result2)
#
# result3 = "Name: {}; age: {}" .format(name, age)
# print(result3)
#
# result4 = "Name: {1}; age: {0}" .format(name, age)
# print(result4)

#----------------------------

l = []
for i in range(32,127):
    l.append(chr(i))
    #print(t)
    b = ''.join(l)
    print(b)


