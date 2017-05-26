import sqlite3

db = sqlite3.connect('db.sqlite3')

cursor = db.cursor()
#c1 = cursor.execute("select * from students")
# print(c1)
# print(c1.fetchone())
# print(c1.fetchone())
# print(c1.fetchmany(2))
# print(c1.fetchall())

# for row in c1:
#     print(row)

cursor.execute("insert into students (name, subj, mark) values (?,?,?)", ('Bob', 'Math', 4))
db.commit()

c1 = cursor.execute("select * from students")
for row in c1:
    print(row)

fields = ('id', 'name', 'subj', 'mark')
#zip(fields, row)
l1 = list(zip(fields,row))
d1 = dict(zip(fields,row))

print(l1)
print(d1)

db.close()

