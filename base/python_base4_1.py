# добавить введение моего числа перед числом компьютера = чтобы он сам вводил большие и маленькие символы

import random


left_value = 1
right_value = 10


while True:
    computer = random.randint(left_value,right_value)
    print(computer)
    my_number = input(int('my_number:'))
    symbol = input('symbol:')
    if symbol == ('='):
        print('Correct')
        break
    if symbol == '>':
        print('My value more than yours')
        left_value = computer+1
        continue
    if symbol == '<':
        print('My value less than yours')
        right_value = computer-1
        continue




# MAX_TRIES = 5 # константа. Константы пишутся большими буквами по PEP
# secret = random.randint(1, 10)
#
# tries = 0
# #is_guessed = False # флаговая переменная
#
# while tries < MAX_TRIES:
#     try:
#         guess = int(input('?'))
#     except ValueError:
#         continue # позволит вернуться обратно к while если пользователь ввел неправильно
#     tries +=1
#     if secret == guess:
#         print('ok')
# #        is_guessed = True
#         break # позволит прервать цикл while
#     if secret < guess:
#         print('<')
#     else:
#         print('>')
# #if not is_guessed:
# else:
#     print("You are looser")