# 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01

change = float(input())  # 1.23

coins_count = 0
while change > 0:

    if change >= 2.00:
        change -= 2.00
    elif change >= 1.00:
        change -= 1.00
    elif change >= 0.50:
        change -= 0.50
    elif change >= 0.20:
        change -= 0.20
    elif change >= 0.10:
        change -= 0.10
    elif change >= 0.05:
        change -= 0.05
    elif change >= 0.02:
        change -= 0.02
    elif change >= 0.01:
        change -= 0.01

    coins_count += 1
    change = round(change, 2)  # round(0.22999999998, 2) == 0.23

print(coins_count)