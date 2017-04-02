# length 5
# get length 4 and check from both sides
# get length 3 and check from left side +1
#
# s = input("Enter string:")
#
# length = len(s)
# print(length)
# while True:
#     full_polindrom = s[::-1]
#     if s == full_polindrom:
#         print('Full polidrom found')
#     else:
#         for i in range(length):
#             s = s[0:length-i+1]
#             full_polindrom = s[::-1]
#             if s == full_polindrom:
#                 print('found polidrom', s)
#         break


s = input("Enter string:")
is_found = False

for k in range(len(s) - 1):
    for i in range(k + 1):
        candidate = s[i: len(s) - k + i]
        if candidate == candidate[::-1]:
            print(candidate)
            is_found = True
            break
    if is_found:
        break