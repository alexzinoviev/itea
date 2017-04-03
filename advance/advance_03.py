f = open('file.txt', 'wt')
print(f)

f.write('string1\n')
f.write('string2\n')
f.write('string3\n')
f.write('строка4\n')
f.close()

#--------------------

#f = open('file.txt', 'rt')
# s = f.read()
# print(s)
#
# f = open('file.txt', 'wt')
# f.write('string4\n')
# f.close()
#
# f = open('file.txt', 'rt')
# s = f.read()
# print(s)


#------------------------------------------
#f = open('file.txt', 'rt')
# print(f.readline())
# print(f.readline())

#------------------------------------------
#f = open('file.txt', 'rt')
# print(f.read(5)) # чтение в байтовом режиме
# print(f.read(5))
# print(f.read(5))

#------------------------------------------
f = open('file.txt', 'rt')
for line in f:
    print(line)


#----------------------------------------------------------------------------------