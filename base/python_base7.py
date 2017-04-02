f = open('file.txt','wt')
f.write('string1\n')
f.write('string2\n')
f.write('string3\n')
f.close()

f = open('file.txt','rt')
s = f.read()
print(s)
f.close()

f = open('file.txt', 'rt')
t = f.read(5)
t1 = f.read(5)
t2 = f.read(5)
print(t)
print(t1)
print(t2)


f = open('file1.txt', 'rt')
f.readline()

f = open('file1.txt', 'rt')
for line in f:
    print(f)


f = open('file1.txt', 'at')
f.tell()
f.write('String6\n')
f.close()



f = open('file.txt', 'r+t')
print(f.tell())
print(f.seek(5))
print(f.tell())
print(f.readline())
print(f.tell())
print(f.seek(-5))
f.close()
print(f.closed)


#-----
# безопасность закрытия файла, всегда файл будет закрываться

with open('file.txt', 'rt') as f:
    for line in f:
        print(line)
print(f.closed)
#---------


import pickle
obj = [1,2,'aaa', [1,2,3]]
print(pickle.dumps(obj))
s = pickle.dumps(obj) # сериализация
print(s)
obj1 = pickle.loads(s) # десериализация
print(obj1)
print(obj == obj1)
print(obj is obj1)


#-----
import pickle
obj = [1,2,'aaa', [1,2,3]]
pickle.dump(obj, open('obj.pickle', 'wb'))
obj1 = pickle.load(open('obj.pickle', 'rb'))
print(obj1)