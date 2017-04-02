l = [1,2,3,4,5,6,8,1,4]
d = {}
for i in l:
    if i in l:
        print(i)
        print(d)
        break
    d[i] = True
    print(d)