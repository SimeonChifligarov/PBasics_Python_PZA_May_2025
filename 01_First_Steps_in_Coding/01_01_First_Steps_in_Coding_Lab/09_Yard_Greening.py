# 1.
sq_meters_greening = float(input())

# 2.
price_before_discount = sq_meters_greening * 7.61
discount = price_before_discount * 0.18

final_price = price_before_discount - discount

# 3.
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
