# - размен монет переписать со списком
coins = [100, 50, 25, 5, 1]

while True:
    try:
        amount = float(input('amount=')) * 100
        break
    except ValueError as e:
        print('Invalid input')

for coin in coins:
    if amount // coin:
        if coin == 100:
            message = '1 grn'
        else:
            message = str(coin) + ' kop'
        print(message, amount // coin)
    amount %= coin