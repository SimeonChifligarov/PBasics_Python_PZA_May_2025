color = input()
flower_count = int(input())
budget = int(input())

price = 0.0

if color == 'Roses':
    price = 5.00
    if flower_count > 80:
        price *= 0.90  # price = price * 0.90  => price = 5.00 * 0.90

elif color == 'Dahlias':
    price = 3.80
    if flower_count > 90:
        price *= 0.85

elif color == 'Tulips':
    price = 2.80
    if flower_count > 80:
        price *= 0.85

elif color == 'Narcissus':
    price = 3.00
    if flower_count < 120:
        price *= 1.15

elif color == 'Gladiolus':
    price = 2.50
    if flower_count < 80:
        price *= 1.20

money_needed = flower_count * price

if money_needed <= budget:
    diff = budget - money_needed
    print(f'Hey, you have a great garden with {flower_count} {color} and {diff:.2f} leva left.')
else:
    diff = money_needed - budget
    print(f'Not enough money, you need {diff:.2f} leva more.')
