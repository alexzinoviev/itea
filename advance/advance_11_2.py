import multiprocessing
import time
import urllib.request

# def double(x):
#     return 2 * x
#
# p = multiprocessing.Pool(4)
# k = p.map(double, range(50))
# print(k)
#
# k1 = p.map(double, [1,2,3,4,5,6,7,8,9])
# print(k1)

#-----------------

# def double_a(x):
#     if x % 4:
#         time.sleep(1)
#     return 2 * x
#
# p = multiprocessing.Pool(4)
# k2 = p.map(double_a, range(50))
# print(k2)

#-----------------


def get_url(url):
    r = urllib.request.urlopen(url)
    return len(r.read())

p = multiprocessing.Pool(4)
t = p.map(get_url, ['http://mail.ru'] * 20)

print(t)