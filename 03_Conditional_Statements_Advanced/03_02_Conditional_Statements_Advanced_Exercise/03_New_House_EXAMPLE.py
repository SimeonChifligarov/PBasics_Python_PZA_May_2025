color = input()
flower_count = int(input())
budget = int(input())

price = 0.0

if color == 'Roses':
    price = ...
    if ...:
        ...
elif color == 'Dahlias':
    price = ...
elif color == 'Tulips':
    price = ...
elif color == 'Narcissus':
    pass
elif color == 'Gladiolus':
    pass

money_needed = flower_count * price

if money_needed <= budget:
    diff = budget - money_needed
    print(f'Hey, you have a great garden with {flower_count} {color} and {diff:.2f} leva left.')
else:
    diff = money_needed - budget
    print(f'Not enough money, you need {diff:.2f} leva more.')
