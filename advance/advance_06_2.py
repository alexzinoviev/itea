# class MyList(list):
#     def sum(self):
#         s = 0
#         for i in self:
#             s+= i
#         return s
#

# l = MyList([2,3,5])
#
# print(dir(l))
# print(l.sum())


# UserList, UserDict, UserData


import collections
class MyList(collections.UserList):
    def sum(self):
        s = 0
        for i in self.data:
            s+= i
        return s


l = MyList([2,3,5])

print(dir(l))
print(l.sum())