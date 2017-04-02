import re
s = 'njhvjkdshvkjhdjfhsdkjfhsdjhfjk dsfdksjhf122--32-45jkdshf  dsjfh234 3234jkdhfkjdhfkjds nj'
t = re.findall('[0-9]{3}[- ]+[0-9]{2}-?[0-9]{2}', s)
print(t)

c = re.compile('[0-9]{3}[- ]+[0-9]{2}-?[0-9]{2}',)
c1 = c.findall(s)
print(c1)