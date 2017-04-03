# f = open('file.txt', 'wt')
# print(f)
#
# f.write('string1\n')
# f.write('string2\n')
# f.write('string3\n')
# f.write('строка4\n')
# f.close()

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
# f = open('file.txt', 'rt')
# for line in f:
#     print(line)
# print(f.closed)

# ------------------------------------------
#гарантировано поможет закрыть файл
# with open('file.txt', 'rt') as f:
#     for line in f:
#         print(line)
# print(f.closed)

#----------------------------------------------------------------------------------

# import pickle
# obj = {'a': [1,2,3], True: 2.345}
# a = pickle.dumps(obj)
# print(a)
# pickle.dump(obj, open('obj.pickle', 'wb'))
# b = pickle.loads(a)
# print(b)
# print(obj == b)

#----------------------------JSON------------------------------------------------------

# import json
# obj = {1: (1,2,3), 'a': [2,3,4], False: None}
# a = json.dumps(obj) # преобразование в строку json
# print(a)
# b = json.loads(a) # преобразование из строки json
# print(b)

#--------------------------------------------------------

# import yaml

#--------------------------------------------------------

# import os
#
# print(os.getcwd())
# #os.mkdir('dir1')
# os.chdir('dir1')
# print(os.getcwd())
# open('file1', 'wt')
# open('file2', 'wt')
# print(os.listdir('.'))
# print(os.path.exists('file1'))
# print(os.path.isfile('file1'))
# print(os.path.isdir('file1'))
#
# print(os.path.join('aaa', 'bbb', 'ccc')) # для построения путей
# os.chdir('dir1')
# os.remove('file1')
# os.unlink('file2')
# os.chdir('..')
# os.rmdir('dir1')
#
#

#--------------------------------------------------------

# import tempfile
# f = tempfile.TemporaryFile()
# print(f)
# f.write(b'Hello')
# print(f.read())
# print(f.name)

#--------------------------------------------------------

#
# import io
# s = io.StringIO()
# s.write('Hello')
# s.read()
# print(s.read())

#--------------------------------------------------------
# scan files in directory by mask

import fnmatch, os
for filename in os.listdir('../base'):
    if fnmatch.fnmatch(filename, '*py'):
        print(filename)