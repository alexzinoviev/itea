# найти минимальный и максимальный элемент и поменять местами

my_list = [-67, 2,4,6,8,10,1,14,97,-1,10,-101,-55,188]
length = int(len(my_list))
#is_similar = False
print(my_list)
min_value = my_list[length-1]
min_index = length-1
max_value = my_list[length-1]
max_index = length-1

for i in range(length-1):
    #print("Index:", i, "ELement value:", my_list[i])
    for j in range(i+1,length):
        #print("Index:", j, "ELement value:", my_list[j])
        if my_list[i] < my_list[j]:
            #print("Number:", my_list[i],"index",i, "less than", my_list[j], "index:", j)
            if min_value > my_list[i]:
                min_value = my_list[i]
                min_index = i
                continue
            else:
                continue
for i in range(length-1):
    #print("Index:", i, "ELement value:", my_list[i])
    for j in range(i+1,length):
        #print("Index:", j, "ELement value:", my_list[j])
        if my_list[i] > my_list[j]:
            #print("Number:", my_list[i],"index",i, "more than", my_list[j], "index:", j)
            if max_value < my_list[i]:
                max_value = my_list[i]
                max_index = i
                continue
            else:
                continue
print("Min value is:", min_value, "Index for min value is:", min_index)
print("Max value is:", max_value, "Index for max value is:", max_index)
my_list.pop(max_index)
my_list.pop(min_index)
my_list.insert(max_index,min_value)
my_list.insert(min_index,max_value)
print("List updated, min value placed to max value and vice versa\n",my_list)