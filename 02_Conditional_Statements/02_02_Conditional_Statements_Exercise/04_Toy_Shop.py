trip_cost = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_money = puzzles_count * 2.60 + talking_dolls_count * 3.00 + teddy_bears_count * 4.10 + minions_count * 8.20 + trucks_count * 2.00

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
total_toys_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count
if total_toys_count >= 50:
    total_money *= 0.75  # total_money = total_money * 0.75

# От спечелените пари Петя трябва да даде 10% за наема на магазина.
total_money_after_rent = total_money * 0.90

if total_money_after_rent >= trip_cost:
    money_left = total_money_after_rent - trip_cost
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = trip_cost - total_money_after_rent
    print(f'Not enough money! {money_needed:.2f} lv needed.')