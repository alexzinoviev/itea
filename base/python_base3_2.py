# автомат для ввода денег, номиналы 1 грн 50 25 5 1 коп - выдать деньги оптимальным количеством монет
# перевести число в копейки

coin_100 = 100
coin_50 = 50
coin_25 = 25
coin_5 = 5
coin_1 = 1

try:
    amount = float(input('amount='))
    if amount<0:
        raise ValueError("Amount can't be less then 0")
    amount_validation = amount*100
    if amount * 100 == int(amount_validation):
        print('Number is in correct format: ', float(amount))
    else:
        raise ValueError('Amount in incorrect format, more than two symbols after "."')
except ValueError as e:
    print(e)
else:
    print(amount)
    amount_coins = amount*100
    q_coins_100 = amount_coins // coin_100
    if q_coins_100 >= 1:
        print('Quantity of coins by 1 uah:', int(q_coins_100))
    rest_coins = amount_coins % coin_100
    q_coins_50 = rest_coins // coin_50
    if q_coins_50>=1:
        print('Quantity of coins by 50 kop:', int(q_coins_50))
    rest_coins = rest_coins % coin_50
    q_coins_25 = rest_coins // coin_25
    if q_coins_25>=1:
        print('Quantity of coins by 25 kop:', int(q_coins_25))
    rest_coins = rest_coins % coin_25
    q_coins_5 = rest_coins // coin_5
    if q_coins_5>=1:
        print('Quantity of coins by 5 kop:', int(q_coins_5))
    rest_coins = rest_coins % coin_5
    q_coins_1 = rest_coins // coin_1
    if q_coins_1>= 1:
        print('Quantity of coins by 1 kop:', int(q_coins_1))