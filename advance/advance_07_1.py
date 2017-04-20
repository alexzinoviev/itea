# l = [1,2,3]
# i = iter(l)
# print(i)
# #l.__next__()
# print(i.__next__())
#
# print(i.__next__())
#
# print(i.__next__())
#
# print(i.__next__())
#

#----------------
def f():
    for i in range(5):
        yield i # принцип работы как и у return  но пускает выполнение дальше и продолжает работу начиная с последнего элемента

        print("Here")

for i in f():
    print(i)

print("----------------------")

g = f()
for i in g:
    if i > 2:
        break
    print(i)

print("----------------------")

for i in g:
    print(i)


#--------------------------
# генератор генератора
l = (x * x for x in range(10))
print(l)

print(next(l))
print(next(l))
print(next(l))