# operator try
# x = 1
# try:
#     a = 5 /x
#     raise ValueError ('my new error')
# except ZeroDivisionError:
#     print('Zero')
# except NameError:
#     print('Name error\n')
#     exit() # interapt application and close
# # except ValueError:
# #     print('Value error')
# except Exception as e:
#     print(e)
# else:
#     print('Ok\n', a)
# finally: # work always, in any situation
#     print('The end')
# print('End of the End\n')


# ввести числа a b c , убедится что это числа, убедится что a > 0 b > 0 c > 0 - если ок - то площадь, если нет ошибка

a = input('a=')
b = input('b=')
c = input('c=')

try:
    float(a)
    a = float(a)
except ValueError:
    print('Value error for A')
try:
    float(b)
    b = float(b)
except ValueError:
    print('Value error for B')
try:
    float(c)
    c = float(c)
except ValueError:
    print('Value error for C')

if a>0:
    print("a>0, let's go to next step")
else:
    raise ValueError('a < 0')
if b>0:
    print("b>0")
else:
    raise ValueError('b<0')
if c>0:
    print("c>0")
else:
    raise ValueError('c<0')

p = (a + b + c) / 2
print(p)
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(S)

if a+b> c and b+c > a and c+a > b:
    print("triangle exist")
else:
    print("triangle doesn't exist")

#----- refactored

try:
    a = float(input('a='))
    b = float(input('b='))
    c = float(input('c='))
    if a<0 or b<0 or c<0:
        raise ValueError('a,b,c<0')
    if a+b <=c or a+c <=b or b+c<=a:
        raise ValueError("triandle doesn't exist")
except ValueError as e:
    print(e)
else:
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Triangle exist", S)