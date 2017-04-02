# # найти пару одинаковых чисел
#
my_list = [2,4,6,8,10,12,14,10]
length = int(len(my_list))
is_similar = False
print(my_list)

for i in range(length-1):
    for j in range(i+1,length):
        if my_list[i] == my_list[j]:
            print("We have similar values:", my_list[i],"index",i, "and",j)
            is_similar = True
            continue
if not is_similar:
    print("All elements are unique")