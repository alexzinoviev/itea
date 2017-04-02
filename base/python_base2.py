#task1

# a = input('a=')
# b = input('b=')
# c = a
# a = b
# b = c
# print ('a=', a)
# print ('b=', b)


#task2
# a = input('a=')
# b = input('b=')
# c = input('c=')
# c1 = c
# c = a
# a = b
# b = c1
# print('a=', a)
# print('b=', b)
# print('c=', c)

#task3
# 10 symbols
# 3  first symbols to end
# 3 last to start
# 4 symbols revert

# a = input('a =')
# b = a[0:3]
# c = a[-3:]
# d = a[3:-3]
# e = d[::-1]
# revert = c+e+b
# print(revert)

# в одну строчку записать

# формула герона

# a = int(input("side a="))
# b = int(input("side b="))
# c = int(input("side c="))
# p = (a+b+c)/2
#
# S = (p*(p-a)*(p-b)*(p-c))**0.5
#
#
# print("p=",p)
# print("S=", S)


#каждая пара сторон больше чем третяя сторона = значит треугольник существует
# task4
a = int(input("side a="))
b = int(input("side b="))
c = int(input("side c="))
p = (a+b+c)/2

S = (p*(p-a)*(p-b)*(p-c))**0.5

one_side = a+b > c
second_side = b+c > a
third_side = c+a > b

print(one_side)
print(second_side)
print(third_side)
rect_exist = one_side and second_side and third_side

print("p=",p)
print("S=", S)
print("Rectangle exist:", rect_exist)

exist2 = S * rect_exist + (-1)*(not rect_exist)
print("Rectangle exist2",exist2)