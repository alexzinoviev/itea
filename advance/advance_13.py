"""
https://habrahabr.ru/post/136305/
теорема CAP
C - consistency
A - avaliability
P - Partition Tolerance


CA - SQL
AP - NoSQL (Not Only SQL)

в одно и то же время мы можем получить доступ только к двум элементам из трех
"""

import pymongo

m = pymongo.MongoClient()



m.test.users.insert({'a': 1, 'l': [1,2,3], 'd': {'q':3, 'w': 'qwe'}})

# m.test.user.find()
# for d in m.test.user.find()
#     print(d)