import collections

#
# d = {}
# if 1 in d:
#     d[1] += 1
# else:
#     d[1] = 1
#
#
# d = collections.defaultdict(int)
# d[1] += 1


d = {}
d.setdefault(1,0)
print(d)
d.setdefault(1,0)
print(d)
d[1] += 1
print(d)
d[1] += 1
print(d)

d[1] += 1
print(d)


t = collections.Counter('hjksdhfkjsdgggf')
print(t)
print(t.most_common())


