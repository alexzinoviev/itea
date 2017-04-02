# #цикл
# i = 0
# while i<5:
#     print(i)
#     i = i+1


import random

MAX_TRIES = 5 # константа. Константы пишутся большими буквами по PEP
secret = random.randint(1, 10)

tries = 0
#is_guessed = False # флаговая переменная

while tries < MAX_TRIES:
    try:
        guess = int(input('?'))
    except ValueError:
        continue # позволит вернуться обратно к while если пользователь ввел неправильно
    tries +=1
    if secret == guess:
        print('ok')
#        is_guessed = True
        break # позволит прервать цикл while
    if secret < guess:
        print('<')
    else:
        print('>')
#if not is_guessed:
else:
    print("You are looser")