# найти минимальный и максимальный элементы

my_list = [103,99,2,101,1,67,4,22,8,199,99,244,10,12,14,16,18,-1,20,210]
#my_list = range(2,110,3)
i = 0
length = int(len(my_list))
element_last = my_list[length-1]
element_first = my_list[0]
for i in my_list:
    element = i
    if element < element_last:
        print("Number " + str(element) + "less than " + str(element_last))
        continue
    else:
        element_last = element
        print("Element last updated to:", element_last)
        continue
for i in my_list:
    element = i
    if element > element_first:
        print("Number " + str(element) + "more than " + str(element_last))
        continue
    else:
        element_first = element
        print("\nElement first updated to:", element_first)
        continue
element_max = element_last
element_min = element_first
print("Max element is: ", element_max, "Min element is: ", element_min)