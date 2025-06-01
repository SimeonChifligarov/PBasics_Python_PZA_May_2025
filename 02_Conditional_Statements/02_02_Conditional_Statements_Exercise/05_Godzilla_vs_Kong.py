budget = float(input())
walk_on = int(input())
price_per_one_walk_on = float(input())

decor = budget * 0.10
discount = 0.0
if walk_on > 150:
    discount = 0.10

price_per_one_walk_on_after_discount = price_per_one_walk_on * (1 - discount)
clothes_price = walk_on * price_per_one_walk_on_after_discount
total_cost = decor + clothes_price

if total_cost > budget:
    money_needed = total_cost - budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    money_left = budget - total_cost
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
