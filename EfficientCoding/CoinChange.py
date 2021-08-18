def coin_change(amount, change):
    if amount in change:
        return 0, amount

    chosen_coin = 0
    for coin in change:
        if coin < amount:
            chosen_coin = coin
            break

    return amount-chosen_coin, chosen_coin


remaining_amount = 8
change = [1, 5, 3, 6]
change.sort()
change.reverse()
coin_chosen = []
while True:
    print("remaining amount is: {}".format(remaining_amount))
    remaining_amount, chosen = coin_change(remaining_amount, change)
    coin_chosen.append(chosen)
    if remaining_amount == 0:
        break

print(coin_chosen)
