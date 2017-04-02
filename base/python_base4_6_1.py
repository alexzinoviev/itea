# найти минимальный и максимальный элемент и поменять местами
l = [1,3,5,7,8,4,5,10,8]

min_ = max_ = l[0]
min_i = max_i = 0

for index, value in enumerate(l):
    if max_ < value:
        max_ = value
        max_i = index
    if min_ > value:
        min_ = value
        min_i = index
l[min_i] = max_
l[max_i] = min_
print(l)