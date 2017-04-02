# - размен монет переписать со списком
COIN_100 = 100
COIN_50 = 50
COIN_25 = 25
COIN_5 = 5
COIN_1 = 1

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
    while True:
        if amount_coins >= 100:
            q_coins = amount_coins // COIN_100
            amount_coins = amount_coins % COIN_100
            print('Quantity of coins by 1 uah:', int(q_coins))
        if 50 <= amount_coins < 100:
            q_coins = amount_coins // COIN_50
            amount_coins = amount_coins % COIN_50
            print('Quantity of coins by 50 kop:', int(q_coins))
        if 25 <= amount_coins < 50:
            q_coins = amount_coins // COIN_25
            amount_coins = amount_coins % COIN_25
            print('Quantity of coins by 25 kop:', int(q_coins))
        if 5 <= amount_coins < 25:
            q_coins = amount_coins // COIN_5
            amount_coins = amount_coins % COIN_5
            print('Quantity of coins by 5 kop:', int(q_coins))
        if 1 <= amount_coins < 5:
            q_coins = amount_coins // COIN_1
            amount_coins = amount_coins % COIN_1
            print('Quantity of coins by 1 kop:', int(q_coins))
        else:
            break
