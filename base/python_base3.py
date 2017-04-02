#
# x = int(input('x:'))
# y = int(input('y:'))
# if x>y:
#     print('x:',x)
# else:
#     if x==y:
#         print('Error')
#     else:
#         print('y:',y)


# x = int(input('x:'))
# y = int(input('y:'))
# if x>y:
#     print('x:',x)
# elif x==y:
#     print('Error')
# else:
#     print('y:',y)

# найти большее из 3 чисел
# x = int(input('x:'))
# y = int(input('y:'))
# z = int(input('z:'))
# if x>y:
#     print('x more y')
#     if x>z:
#          print('x more z', x)
#     else:
#          print('z more x', z)
# elif x<y:
#     print('y more x')
#     if y>z:
#         print('y more z', y)
#     else:
#         print('z more x', z)

# найти большее из 3 чисел c равенством
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
if x>y:
    print('x more y')
    if x>z:
         print('x more z', x)
    else:
         print('z more x', z)
elif x<y:
    print('y more x')
    if y>z:
        print('y more z', y)
    else:
        print('z more x', z)
elif y==x==z:
    print('all numbers are the same')
elif x==y:
    print('x = y')
    if x>z:
        print('x and y more z', x)
    else:
        print('z more x', z)
elif x==z:
    print('x = z')
    if x>y:
        print('x and z more than y', x)
    else:
        print('y more', y)
else:
    if y==z:
        print('y = z')
    elif y>x:
        print('y and z more than x', y)
    else:
        print('x more', x)